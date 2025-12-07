from django.urls import path
from .views import (
    get_homes, get_home,
    create_home, update_home, delete_home
)

urlpatterns = [
    path('get_homes/', get_homes, name='get-homes'),
    path('create_home/', create_home, name='create-home'),
    path('get_home/<int:pk>/', get_home, name='get-home'),
    path('update_home/<int:pk>/', update_home, name='update-home'),
    path('delete_home/<int:pk>/', delete_home, name='delete-home'),
]
