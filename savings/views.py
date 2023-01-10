from rest_framework import generics
from .serializers import SavingSerializer
from .models import Saving


class SavingView(generics.ListCreateAPIView):
    serializer_class = SavingSerializer

    queryset = Saving.objects.all()


class SavingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SavingSerializer

    queryset = Saving.objects.all()

    lookup_url_kwarg = "saving_id"
