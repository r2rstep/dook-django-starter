from rest_framework import generics

from .models import Item
from .serializers import ItemSerializer


class ItemView(generics.ListCreateAPIView,
               generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filterset_fields = ['prop']
