from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from users.models import User
from users.serializers import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    """Контроллер пользователя"""
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = request.data["password"]
        user = serializer.instance
        user.is_active = True
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]
