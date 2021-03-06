from django.urls import path

from blogs.api import BlogsListAPIView, UserBlogAPIView
from blogs.views import BlogsListView, UserBlogView

urlpatterns = [
    path('blogs/<str:username>', UserBlogView.as_view(), name="user_blog"),
    path('blogs', BlogsListView.as_view(), name="blogs_list"),

    #API
    path('api/v1/blogs/<str:username>/', UserBlogAPIView.as_view(), name='user_blog_api'),
    path('api/v1/blogs/', BlogsListAPIView.as_view(), name='blogs_list_api')
]