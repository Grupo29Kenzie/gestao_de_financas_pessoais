from rest_framework import generics
from .models import ExpenseEntrie
from .serializers import ExpenseEntrieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAuthenticated, IsAccountOwner, IsExpenseEntrieOwner

class ExpenseEntrieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    serializer_class= ExpenseEntrieSerializer
    queryset = ExpenseEntrie.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

    def get_queryset(self):
          return ExpenseEntrie.objects.filter(user_id=self.request.user.id)

class ExpenseEntrieDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsExpenseEntrieOwner]

    serializer_class = ExpenseEntrieSerializer
    queryset = ExpenseEntrie.objects.all()

    lookup_url_kwarg = "pk"

class ExpenseEntrieMonthExpirationView(generics.ListAPIView):
    ...


    
        
        