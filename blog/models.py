import readtime
from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

STATUS = (
    (0, 'Draft'),
    (1, 'Publish'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(default='')
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    comments_count = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_read_time(self):
        read_time = readtime.of_text(self.content)
        return read_time


class Comment(models.Model):
    username = models.CharField(max_length=255, verbose_name='Name')
    content = models.TextField(verbose_name='Comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email


class Setting(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about[:20] + '...'
