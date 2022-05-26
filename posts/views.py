from rest_framework import generics
from .serializers import PostSerializer
from .models import Posts
# Create your views here.

class PostList(generics.ListAPIView):
    """
    List all posts
    """
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    """
    List a single post
    """
    queryset = Posts.objects.all()
    serializer_class = PostSerializer