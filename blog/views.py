import os
import smtplib
from email.message import EmailMessage

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from blog.forms import ProfileForm, UserForm, CommentForm, ContactForm
from blog.models import Post, Profile, Comment, Contact, Setting, Category, DownloadFiles


class Posts(View):
    def get(self, *args, **kwargs):
        post_list = Post.objects.filter(status=1)
        settings = Setting.objects.all()
        context = {
            'post_list': post_list,
            'settings': settings,
        }
        return render(self.request, 'blog/index.html', context)
    # template_name = 'blog/index.html'
    # queryset = Post.objects.filter(status=1)


class PostDetails(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-added_on')
        number_of_comments = comments.count()
        post.comments_count = number_of_comments
        post.save()

        settings = Setting.objects.all()
        context = {
            'post': post,
            'form': form,
            'comments': comments,
            'settings': settings,
            'number_of_comments': number_of_comments,
        }
        return render(request, 'blog/details.html', context)

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            content = form.cleaned_data.get('content')
            comment = Comment()
            comment.username = username
            comment.content = content
            comment.post = post
            comment.save()
            return redirect('blog:details', slug=slug)


def register(request):
    logout(request)
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        context = {
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'password1': password1,
            'password2': password2,
        }

        if password1 != password2:
            messages.warning(request, "Passwords do not match.")
            return render(request, "blog/register.html", context)
        try:
            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            messages.success(request, 'Successfully logged in.')
        except IntegrityError:
            messages.warning(request, "Username already taken.")
            return render(request, "blog/register.html", context)

        return redirect('blog:posts')

    return render(request, "blog/register.html")


def login_user(request):
    logout(request)
    if request.method == "POST":
        return_url = request.POST.get("return_url")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "Successfully logged in")
                if return_url:
                    return HttpResponseRedirect(return_url)
                else:
                    return redirect("/")
        else:
            messages.warning(request, "Invalid username or password")
        return redirect('blog:login')
    return render(request, "blog/login.html")


class ProfileUpdate(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request, "blog/profile.html")

    def post(self, *args, **kwargs):
        try:
            profile = self.request.user.profile
        except Profile.DoesNotExist:
            profile = Profile(user=self.request.user)
        form = ProfileForm(data=self.request.POST, files=self.request.FILES, instance=profile)
        u_form = UserForm(data=self.request.POST, files=self.request.FILES, instance=self.request.user)
        if form.is_valid() and u_form.is_valid():
            form.save()
            u_form.save()
            messages.success(self.request, 'Profile successfully updated.')
            return redirect('blog:profile')


@login_required(login_url='blog:login')
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    form = ProfileForm(instance=profile)
    u_form = UserForm(instance=request.user)
    return render(request, "blog/edit_profile.html", {'form': form, 'u_form': u_form})


@login_required(login_url='blog:login')
def user_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('blog:posts')


class UserContact(View):
    def get(self, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(self.request, 'blog/contact.html', context)

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            contact = Contact()
            contact.email = email
            contact.message = message
            contact.save()
            send_mail(os.environ.get('EMAIL_HOST_USER'), os.environ.get('EMAIL_HOST_PASSWORD'))
            messages.success(self.request, 'Message sent successfully.')
            return redirect('blog:contact')
        else:
            messages.warning(self.request, 'Message not sent, enter a valid email.')
            return redirect('blog:contact')


class Settings(View):
    def get(self, *args, **kwargs):
        settings = Setting.objects.all()
        context = {
            'settings': settings
        }
        return render(self.request, 'blog/settings.html', context)


def like_post(request, slug):
    post = Post.objects.get(slug=slug)
    ip = request.META.get('REMOTE_ADDR')
    # if ip not in remote_addresses_likes:
    post.likes += 1
    # post.like_button_color='color:red'
    ip = request.META.get('REMOTE_ADDR')
    # remote_addresses_likes.append(ip)
    post.save()
    return redirect('blog:posts')


def dislike_post(request, slug):
    post = Post.objects.get(slug=slug)
    ip = request.META.get('REMOTE_ADDR')
    # if ip not in remote_addresses_dislikes:
    post.dislikes += 1
    # post.dislike_button_color='color:red'
    ip = request.META.get('REMOTE_ADDR')
    # remote_addresses_dislikes.append(ip)
    post.save()
    return redirect('blog:posts')


def like_post_details(request, slug):
    post = Post.objects.get(slug=slug)
    ip = request.META.get('REMOTE_ADDR')
    # if ip not in remote_addresses_likes:
    post.likes += 1
    # post.like_button_color='color:red'
    ip = request.META.get('REMOTE_ADDR')
    # remote_addresses_likes.append(ip)
    post.save()
    return redirect('blog:details', slug=slug)


def dislike_post_details(request, slug):
    post = Post.objects.get(slug=slug)
    ip = request.META.get('REMOTE_ADDR')
    # if ip not in remote_addresses_dislikes:
    post.dislikes += 1
    # post.dislike_button_color='color:red'
    ip = request.META.get('REMOTE_ADDR')
    # remote_addresses_dislikes.append(ip)
    post.save()
    return redirect('blog:details', slug=slug)


class PostCategory(View):
    def get(self, request, category, *args, **kwargs):
        posts = Post.objects.filter(category__name__contains=category, status=1)
        settings = Setting.objects.all()
        context = {
            'post_list': posts,
            'category': category,
            'settings': settings,
        }
        return render(self.request, 'blog/category.html', context)


def all_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def send_mail(email_address, email_password):
    """Sending emails with Html format."""
    msg = EmailMessage()
    msg['Subject'] = 'New Message Blog'
    msg['From'] = email_address
    msg['To'] = ['erastusnzula@gmail.com']
    msg.set_content('''
    <!DOCTYPE html>
    <html>
        <body>
        <p>Hey, check admin portal a new person contacted you.</p>
        </body>
    </html>
    ''', subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)


class Download(View):
    def get(self, *args, **kwargs):
        files = DownloadFiles.objects.all()
        context = {
            'files': files
        }
        return render(self.request, 'blog/download.html', context)
