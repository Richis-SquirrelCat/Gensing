from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *


# Create your views here.

@api_view(["GET"])
def info_social(request):
    info = Info.objects.last()
    info_ser = InfoSerializer(info)
    s_media = SocialMedia.objects.all()
    s_media_ser = SocialMediaSerializer(s_media, many=True)
    data = {
        "info": info_ser.data,
        "social_media": s_media_ser.data
    }
    return Response(data)

@api_view(['GET'])
def product(request):
    product = Product.objects.order_by('-id')[:2]
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)


@api_view(['POST'])
def post_order(request):
    name = request.POST.get("name")
    phone_number = request.POST.get("phone_number")
    if name and phone_number is not None:
        if name.isalpha():
            if len(phone_number) == 13:
                if phone_number[:4] == "+998":
                    a = phone_number[4:6]
                    list = ["99", "98", "97", "95", "94", "93", "91", "90", "88", "33"]
                    if a in list:
                        if phone_number[6:].isdigit():
                            Order.objects.create(name=name, phone=phone_number)
                            order = Order.objects.last()
                            data = OrderSerializer(order).data
                        else:
                            data = {
                                "error": "Number must include only numbers"
                            }
                    else:
                        data = {
                            "error": "Number company not found"
                        }
                else:
                    data = {
                        "error": "Ex. +998901234567"
                    }
            else:
                data = {
                    "error": "The length of number must be 13"
                }
        else:
            data = {
                "error": "Name must include only letters"
            }
    else:
        data = {
            "error": "Name and number can't be None"
        }
    return Response(data)



@api_view(['GET'])
def get_order(request):
    order = Order.objects.all()
    ser = OrderSerializer(order)
    return Response(ser.data)

@api_view(['GET'])
def discount(request):
    dis = Discount.objects.last()
    ser = DiscountSerializer(dis)
    return Response(ser.data)


@api_view(['GET'])
def about_product(request):
    prod = AboutProduct.objects.order_by('-id')[:2]
    ser = AboutProductSerializer(prod, many=True)
    return Response(ser.data)


@api_view(['GET'])
def about_company(request):
    comp = AboutCompany.objects.last()
    ser = AboutCompanySerializer(comp)
    return Response(ser.data)



@api_view(['GET'])
def faq(request):
    faq = Faq.objects.order_by('-id')[:3]
    ser = FaqSerializer(faq, many=True)
    return Response(ser.data)


@api_view(['GET'])
def how_using(request):
    who_use = WhoUse.objects.all()
    who_use_ser = WhoUseSerializer(who_use, many=True)
    data = {
        "data": who_use_ser.data,
    }
    return Response(data)


@api_view(['GET'])
def using(request):
    use = WhoUse.objects.order_by('-id')[:7]
    ser = WhoUseSerializer(use, many=True)
    return Response(ser.data)


@api_view(['GET'])
def info(request):
    info = Info.objects.last()
    ser = InfoSerializer(info)
    return Response(ser.data)

