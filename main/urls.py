from django.urls import path
from .views import *

urlpatterns = [
    path('start/', start),
    path('product/', product),
    path('post-order/', post_order),
    path('discount/', discount),
    path('about-product/', about_product),
    path('about-company/', about_company),
    path('using/', using),
    path('faq/', faq),
    path('product-cooking/', product_cooking),
    path('recommend/', recommend),
    path('info/', info),
]