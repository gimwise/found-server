from .models import Favorites, Locker, MeMo
from .serializers import FavoriteSerializer, LockerSerializer, MemoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from rest_framework.response import Response

class LockerViewSet(ModelViewSet):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer

class MemoViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MeMo.objects.all()
    serializer_class = MemoSerializer
    
class FavoriteViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Favorites.objects.all()
    serializer_class = FavoriteSerializer