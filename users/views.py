from .models import User
from .serializers import UserSerializer

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAuthenticated, IsAccountOwner

class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "user_id"
