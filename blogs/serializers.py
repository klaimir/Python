from rest_framework import serializers

from blogs.models import Blog
from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ['title', 'image', 'intro', 'publication_date']


class BlogsList(serializers.ModelSerializer):
    user = serializers.CharField()
    title = serializers.CharField()
    url = serializers.HyperlinkedIdentityField(view_name='user_blog', lookup_field='username')

    class Meta:
        model = Blog
        fields = ['user', 'title', 'url']
