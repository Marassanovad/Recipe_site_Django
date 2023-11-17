from enum import Enum

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoryEnum(Enum):
    SOUP = 'soup'
    BREAKFAST = 'breakfast'
    BAKE = 'bake'
    DESERT = 'desert'
    PIZZA = "pizza"
    MILK = "milk"
    SALAD = "salad"
    MEAT = "meat"


CATEGORY_CHOICE = (
    (CategoryEnum.SOUP.value, 'soup'),
    (CategoryEnum.BREAKFAST.value, 'breakfast'),
    (CategoryEnum.BAKE.value, 'bake'),
    (CategoryEnum.DESERT.value, 'desert'),
    (CategoryEnum.PIZZA.value, 'pizza'),
    (CategoryEnum.MILK.value, 'milk'),
    (CategoryEnum.SALAD.value, 'salad'),
    (CategoryEnum.MEAT.value, 'meat'),
)

class Categories(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=50, choices=CATEGORY_CHOICE)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=10)
    products = models.TextField(default='none')
    description = models.TextField(default='none')
    cooking_steps = models.TextField(default='none')
    cooking_time = models.IntegerField(default=10)
    image = models.ImageField(upload_to='products/', default='none', verbose_name='Фото блюда',)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.pk}'
