from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(
        {"posts": serializer.data},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
@permission_classes([AllowAny])
def get_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    serializer = PostSerializer(post)

    return Response(
        {"post": serializer.data},
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(user=request.user)

        return Response(
            { "post": serializer.data },
            status=status.HTTP_201_CREATED
        )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_post(request, pk):
    post = get_object_or_404(Post, id=pk)

    if post.user != request.user:
        return Response(
            {"error": "You do not have permission to edit this post"},
            status=status.HTTP_403_FORBIDDEN
        )

    serializer = PostSerializer(post, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"post": serializer.data},
            status=status.HTTP_200_OK
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)

    if post.user != request.user:
        return Response(
            {"error": "You do not have permission to delete this post"},
            status=status.HTTP_403_FORBIDDEN
        )

    post.delete()
    return Response(
        {"message": "Post deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )
