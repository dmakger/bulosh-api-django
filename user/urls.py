from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserRegistrationView, CurrentUserView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    path('register/', UserRegistrationView.as_view(), name='register'),
    path('current/', CurrentUserView.as_view(), name='current_user'),
]
