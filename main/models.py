from django.db import models


class Start(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='background')
    button = models.CharField(max_length=255)
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class Order(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class Discount(models.Model):
    title = models.CharField(max_length=255)
    first_cost = models.IntegerField()
    last_coat = models.IntegerField()
    benefit = models.IntegerField()
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class Product(models.Model):
    photo = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class About_product(models.Model):
    text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='product/')
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class Product_cooking(models.Model):
    text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='product/')
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class About_company(models.Model):
    text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='company/')
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class Recommend(models.Model):
    title = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='rec/')
    text = models.CharField(max_length=255)
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class Using(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class Faq(models.Model):
    number = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class Info(models.Model):
    logo = models.ImageField(upload_to='logo/')
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    website2 = models.CharField(max_length=255)
    website3 = models.CharField(max_length=255)
    website4 = models.CharField(max_length=255)
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
