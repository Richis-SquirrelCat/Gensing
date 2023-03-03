from rest_framework import serializers
from .models import *


class StartSerializer(serializers.Serializer):
    model = Start
    field = '__all__'


class OrderSerializer(serializers.Serializer):
    model = Order
    field = '__all__'


class DiscountSerializer(serializers.Serializer):
    model = Discount
    field = '__all__'


class ProductSerializer(serializers.Serializer):
    model = Product
    field = '__all__'


class About_productSerializer(serializers.Serializer):
    model = About_product
    field = '__all__'


class Product_cookingSerializer(serializers.Serializer):
    model = Product_cooking
    field = '__all__'


class About_companySerializer(serializers.Serializer):
    model = About_company
    field = '__all__'


class RecommendSerializer(serializers.Serializer):
    model = Recommend
    field = '__all__'


class UsingSerializer(serializers.Serializer):
    model = Using
    field = '__all__'


class FaqSerializer(serializers.Serializer):
    model = Faq
    field = '__all__'


class InfoSerializer(serializers.Serializer):
    model = Info
    field = '__all__'
