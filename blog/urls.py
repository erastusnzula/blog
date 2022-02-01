from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.Posts.as_view(), name='posts'),
    path('<slug:slug>/', views.PostDetails.as_view(), name='details'),
    path('blog/register/', views.register, name='register'),
    path('blog/login/', views.login_user, name='login'),
    path('blog/logout/', views.user_logout, name='logout'),
    path("blog/profile/", views.ProfileUpdate.as_view(), name="profile"),
    path("blog/edit/profile/", views.edit_profile, name="edit-profile"),
    path("blog/user/contact/", views.UserContact.as_view(), name="contact"),
    path("blog/settings/", views.Settings.as_view(), name="settings"),
    path("blog/likes/<slug:slug>/", views.like_post, name="likes"),
    path("blog/post/<slug:slug>/", views.like_post_details, name="likes-details"),
]
