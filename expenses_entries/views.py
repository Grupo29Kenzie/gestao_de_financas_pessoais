from rest_framework import generics
from .models import ExpenseEntrie
from .serializers import ExpenseEntrieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAuthenticated

class ExpenseEntrieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class= ExpenseEntrieSerializer
    queryset = ExpenseEntrie.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
        
        