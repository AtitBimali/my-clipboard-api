# views.py
from rest_framework import generics, permissions
from .models import Clipboard
from .serializers import ClipboardSerializer

class ClipboardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Clipboard.objects.all()
    serializer_class = ClipboardSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClipboardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clipboard.objects.all()
    serializer_class = ClipboardSerializer
    permission_classes = [permissions.IsAuthenticated]
