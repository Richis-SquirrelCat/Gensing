from django.db import models


class Info(models.Model):
    logo = models.ImageField(upload_to='logo/')
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class SocialMedia(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="social_media/")
    link = models.URLField()


class Order(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


class Discount(models.Model):
    foto = models.ImageField(upload_to='discount/')


class Product(models.Model):
    photo = models.ImageField(upload_to='product/')
    cost = models.IntegerField()
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)


class AboutProduct(models.Model):
    photo = models.ImageField(upload_to='product/')
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class AboutCompany(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()


class WhoUse(models.Model):
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)


class HowToUse(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()


class Faq(models.Model):
    number = models.CharField(max_length=255)
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
