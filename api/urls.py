from django.urls import path
from .views import Users

urlpatterns = [
    path('users/', Users.as_view(), name = 'usuarios'),
    path('users/<int:id>/', Users.as_view(), name = 'update-user')
]