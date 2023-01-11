from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Credit_Card
from .serializers import CreditCardSerializer
from users.permissions import IsCreditCardOwner, RoutePermission


class CreditCardView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CreditCardSerializer
    queryset = Credit_Card.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Credit_Card.objects.all()
        else:
            return Credit_Card.objects.filter(user_id=self.request.user.id)



class CreditCardDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsCreditCardOwner]

    serializer_class = CreditCardSerializer
    queryset = Credit_Card.objects.all()

    lookup_url_kwarg = "pk"