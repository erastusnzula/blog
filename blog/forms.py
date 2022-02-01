from django import forms
from django.contrib.auth.models import User

from blog.models import Profile, Comment, Contact


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'facebook', 'instagram', 'twitter', 'image']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'cols': 15, 'placeholder': 'Describe yourself briefly.'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':3, 'cols':15}),
        }




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 15, 'placeholder':'Write your concern here.'}),
            'email': forms.TextInput(attrs={'placeholder': 'example@gmail.com'})
        }
