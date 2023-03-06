from django.urls import path
from .views import *

urlpatterns = [
    path('product/', product),
    path('post-order/', post_order),
    path('get-order/', get_order),
    path('discount/', discount),
    path('about-product/', about_product),
    path('about-company/', about_company),
    path('using/', using),
    path('faq/', faq),
    path('product-cooking/', how_using),
    path('info/', info),
    path('info-social/', info_social)
]
