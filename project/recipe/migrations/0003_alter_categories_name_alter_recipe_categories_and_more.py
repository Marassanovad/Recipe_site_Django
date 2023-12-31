# Generated by Django 4.2.6 on 2023-11-15 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipe", "0002_remove_categories_description_alter_categories_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categories",
            name="name",
            field=models.CharField(
                choices=[
                    ("soup", "soup"),
                    ("breakfast", "breakfast"),
                    ("bake", "bake"),
                    ("desert", "desert"),
                    ("pizza", "pizza"),
                    ("milk", "milk"),
                    ("salad", "salad"),
                    ("meat", "meat"),
                ],
                max_length=50,
                verbose_name="Название категории",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="categories",
            field=models.ForeignKey(
                default="none",
                on_delete=django.db.models.deletion.CASCADE,
                to="recipe.categories",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="cooking_time",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="customer",
            field=models.ForeignKey(
                default="none",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
