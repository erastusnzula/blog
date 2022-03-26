from django.contrib import admin

from blog.models import Profile, Post, Comment, Contact, Setting, Category, DownloadFiles


class PostAdmin(admin.ModelAdmin):
    list_filter = ['status']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug', 'status', 'created_on']


admin.site.register(Profile)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Setting)
admin.site.register(DownloadFiles)
