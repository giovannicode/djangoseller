from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

    picture = serializers.ImageField(use_url=False)
    absolute_url = serializers.URLField(source='get_absolute_url')
