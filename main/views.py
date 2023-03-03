from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import *


# Create your views here.

@api_view(['GET'])
def start(request):
    start = Start.objects.last()
    ser = StartSerializer(start)
    return Response(ser.data)


@api_view(['GET'])
def product(request):
    product = Product.objects.order_by('-id')[:2]
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)


@api_view(['POST'])
def post_order(request):
    name = request.POST.get("name")
    phone_number = request.POST.get("phone_number")
    order = Order.objects.create(name=name, phone_number=phone_number)
    ser = OrderSerializer(order)
    return Response(ser.data)


@api_view(['GET'])
def discount(request):
    dis = Discount.objects.last()
    ser = DiscountSerializer(dis)
    return Response(ser.data)


@api_view(['GET'])
def about_product(request):
    prod = About_product.objects.order_by('-id')[:2]
    ser = About_productSerializer(prod, many=True)
    return Response(ser.data)


@api_view(['GET'])
def about_company(request):
    comp = About_company.objects.last()
    ser = About_productSerializer(comp)
    return Response(ser.data)


@api_view(['GET'])
def using(request):
    use = Using.objects.last()
    ser = UsingSerializer(use)
    return Response(ser.data)


@api_view(['GET'])
def faq(request):
    faq = Faq.objects.order_by('-id')[:3]
    ser = FaqSerializer(faq, many=True)
    return Response(ser.data)


@api_view(['GET'])
def product_cooking(request):
    cook = Product_cooking.objects.last()
    ser = Product_cookingSerializer(cook)
    return Response(ser.data)


@api_view(['GET'])
def recommend(request):
    recommend = Recommend.objects.order_by('-id')[:7]
    ser = RecommendSerializer(recommend, many=True)
    return Response(ser.data)


@api_view(['GET'])
def info(request):
    info = Info.objects.last()
    ser = InfoSerializer(info)
    return Response(ser.data)
