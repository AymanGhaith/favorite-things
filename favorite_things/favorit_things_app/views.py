from rest_framework import viewsets
from .models import FavoriteThing, Category, AuditTrail
from .serializers import FavoriteThingSerializer, CategorySerializer, AuditTrailSerializer

class FavoriteThingViewSet(viewsets.ModelViewSet):
    queryset = FavoriteThing.objects.all()
    serializer_class = FavoriteThingSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuditTrailViewSet(viewsets.ModelViewSet):
    queryset = AuditTrail.objects.all()
    serializer_class = AuditTrailSerializer
