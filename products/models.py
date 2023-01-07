from django.db import models
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name='Название категории'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание категории'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название товара'
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True,
        verbose_name='Изображение '
    )
    description = models.TextField(
        blank=True,
        verbose_name='Полное описание'
    )
    short_description = models.CharField(
        max_length=80,
        blank=True,
        verbose_name='Короткое описание'
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name='Цена'
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество товара'
    )
    category = models.ForeignKey(
        ProductCategory,
        related_name='category',
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    def __str__(self):
        return f'{self.name} | {self.category.name}'
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Basket(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        default=0,
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.product} | {self.quantity}'
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Товары в корзине'
