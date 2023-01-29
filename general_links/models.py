from django.db import models
from django.utils import timezone


class Address(models.Model):
    country = models.CharField(verbose_name="Страна", max_length=50, null=True, blank=True)
    city = models.CharField(verbose_name="Город", max_length=50, null=True, blank=True)
    street = models.CharField(verbose_name="Улица", max_length=50, null=True, blank=True)
    num_house = models.CharField(verbose_name="Номер дома", max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return self.country + self.city


class Contact(models.Model):
    email = models.EmailField(verbose_name="Email", max_length=50, null=True, blank=True)
    address = models.ForeignKey(Address, verbose_name="Адрес", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.address


class Product(models.Model):
    name = models.CharField(verbose_name="Название продукта/товара", max_length=50)
    model = models.CharField(verbose_name="Модель продукта/товара", max_length=50)
    pubdate = models.DateTimeField(verbose_name="Дата выхода продукта/товара на рынок", default=timezone.now)

    class Meta:
        verbose_name = "Продукт/товар"
        verbose_name_plural = "Продукты/товары"

    def __str__(self):
        return self.name


class Provider(models.Model):
    class Name(models.IntegerChoices):
        factory = 1, "Завод"
        distributor = 2, "Дистрибьютор"
        dealership = 3, "Дилерский центр"
        retailer = 4, "Крупная розничная сеть"
        businessman = 5, "Индивидуальный предприниматель"

    name = models.PositiveSmallIntegerField(verbose_name="Наименование поставщика", choices=Name.choices, default=Name.factory)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.name


class LinkModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(verbose_name="Наименование завода", max_length=50)
    contact = models.ForeignKey(Contact, verbose_name="Контакты организации", on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name="Наименование продукта/товара", max_length=50, on_delete=models.PROTECT)
    provider = models.ForeignKey(Provider, verbose_name="Поставщик продукта/товара", null=True, blank=True, on_delete=models.PROTECT)
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Задолженность перед поставщиком",  default=0.00)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата создания организации")

    def __str__(self):
        return self.name


class Factory(LinkModel):
    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class Distributor(LinkModel):
    class Meta:
        verbose_name = 'Дистрибьютор'
        verbose_name_plural = 'Дистрибьюторы'


class Dealership(LinkModel):
    class Meta:
        verbose_name = 'Дилерский центр'
        verbose_name_plural = 'Дилерские центры'


class Retailer(LinkModel):
    class Meta:
        verbose_name = 'Крупная розничная сеть'
        verbose_name_plural = 'Крупные розничные сети'


class Businessman(LinkModel):
    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'

