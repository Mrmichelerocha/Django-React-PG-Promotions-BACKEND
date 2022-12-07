from rest_framework import serializers
from web.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'image', 'price', 'discount', 'content', 'validity', 'author', 'category', 'status')
        model = Post
