from rest_framework import serializers
from .models import *


class SocialMediaSerializer(serializers.Serializer):
    model = SocialMedia
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


class AboutProductSerializer(serializers.Serializer):
    model = AboutProduct
    field = '__all__'



class AboutCompanySerializer(serializers.Serializer):
    model = AboutCompany
    field = '__all__'


class WhoUseSerializer(serializers.Serializer):
    model = WhoUse
    field = '__all__'


class HowToUseSerializer(serializers.Serializer):
    model = HowToUse
    field = '__all__'


class FaqSerializer(serializers.Serializer):
    model = Faq
    field = '__all__'


class InfoSerializer(serializers.Serializer):
    model = Info
    field = '__all__'

