from .models import User
from .serializers import UserSerializer, UserCreateSerializer

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAuthenticated, RoutePermission, IsAccountOwner


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "user_id"
