from django.urls import path
from .views import register_user, get_user, get_users, CustomTokenObtainPairView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('get_users/', get_users, name='get_users'),
    path('get_user/<int:pk>/', get_user, name='get_user'),
    path('register/', register_user, name='register_user'),  # Fixed this line
]

