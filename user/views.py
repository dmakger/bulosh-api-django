from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.serializers import UserRegistrationSerializer, ProfileSerializer
from user.tasks import send_registration_email


# Регистрация
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     user = serializer.save()
        # Получаем email пользователя и отправляем письмо асинхронно
        # send_registration_email.delay(user.email)


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Получаем профиль текущего пользователя
        return self.request.user.profile

    def retrieve(self, request, *args, **kwargs):
        # Получаем сериализованные данные профиля текущего пользователя
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
