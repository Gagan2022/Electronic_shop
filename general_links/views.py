from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from general_links.permissions import IsActivePermission
from general_links.models import LinkModel, Product
from general_links.serializers import LinkSerializer, ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    """Представление для создания продукта"""
    model = Product
    permission_classes = [IsAuthenticated, IsActivePermission]
    serializer_class = ProductSerializer


class ProductView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, обновления и удаления продукта"""
    model = Product
    permission_classes = [IsAuthenticated, IsActivePermission]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter()


class LinkCreateView(generics.CreateAPIView):
    """Представление для создания объекта сети"""
    model = LinkModel
    permission_classes = [IsAuthenticated, IsActivePermission]
    serializer_class = LinkSerializer


class LinkListView(generics.ListAPIView):
    """Представление для просмотра объектов сети в списке"""
    model = LinkModel
    #queryset = LinkModel.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = LinkSerializer
    filterset_fields = ["debt", ]

   
class LinkView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, обновления и удаления объекта сети"""
    model = LinkModel
    permission_classes = [IsAuthenticated, IsActivePermission]
    serializer_class = LinkSerializer

    def get_queryset(self):
        return LinkModel.objects.filter()
