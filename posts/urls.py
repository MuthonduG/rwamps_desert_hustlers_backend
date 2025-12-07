from django.urls import path
from .views import (
    get_posts, get_post, create_post,
    update_post, delete_post
)

urlpatterns = [
    path('get_posts/', get_posts, name='get-posts'),
    path('get_post/<int:pk>/', get_post, name='get-post'),
    path('create_post/', create_post, name='create-post'),
    path('update_post/<int:pk>/', update_post, name='update-post'),
    path('delete_post/<int:pk>/', delete_post, name='delete-post'),
]
