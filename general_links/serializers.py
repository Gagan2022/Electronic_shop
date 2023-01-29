from rest_framework import serializers

from general_links.models import Product, Provider, LinkModel


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор продуктов/товаров"""
    class Meta:
        model = Product
        read_only_fields = ["id"]
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):
    """Сериализатор поставщиков"""
    class Meta:
        model = Provider
        read_only_fields = ["id", "is_active", "is_staff"]
        fields = ["id", "is_active", "is_staff", "username", "first_name", "last_name"]


class LinkSerializer(serializers.ModelSerializer):
    """Сериализатор объекта сети"""
    products = ProductSerializer(many=True)
    providers = ProviderSerializer(many=True)

    class Meta:
        model = LinkModel
        read_only_fields = ["published", "id", "debt"]
        fields = "__all__"
