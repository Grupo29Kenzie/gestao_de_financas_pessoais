from rest_framework import generics
from .serializers import SavingSerializer
from .models import Saving
from users.permissions import IsAuthenticated,IsAccountOwner, RoutePermission,IsSavingOwner
from rest_framework_simplejwt.authentication import JWTAuthentication


class SavingView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, RoutePermission]
    
    serializer_class = SavingSerializer

    queryset = Saving.objects.all()


class SavingDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSavingOwner]
    
    serializer_class = SavingSerializer

    queryset = Saving.objects.all()

    lookup_url_kwarg = "saving_id"
