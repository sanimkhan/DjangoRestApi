from rest_framework import serializers

from .models import Product


class PrimaryProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sales_price',
            'discount'
        ]

    @staticmethod
    def get_discount(obj):
        return obj.get_discount()


class SecondarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sales_price',
        ]
