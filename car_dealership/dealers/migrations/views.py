from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Dealer
from .serializers import DealerSerializer

class DealerListCreate(generics.ListCreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    permission_classes = [IsAuthenticated]

class DealerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    permission_classes = [IsAuthenticated]
