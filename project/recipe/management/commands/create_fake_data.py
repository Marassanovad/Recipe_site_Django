import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from recipe.models import Recipe
from project.recipe.models import Categories





class Command(BaseCommand):
    help = "Generate fake data."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = User(username=f'Name{i}', email=f'mail{i}@mail.ru', password=random.randint(1000000000, 9999999999))
            author.save()
            for i in range(1, count + 1):
                recipe = Recipe(customer=author, categories=random.randint(1, 9), title=f'Name{i}', description=f'NEW PRODUCT', cooking_steps='asdfghjkghjklhjkl',product=f'Name{i}', cooking_time=random.randint(10, 1000))
                recipe.save()