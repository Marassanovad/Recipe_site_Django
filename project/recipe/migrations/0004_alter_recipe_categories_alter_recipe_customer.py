# Generated by Django 4.2.6 on 2023-11-15 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipe", "0003_alter_categories_name_alter_recipe_categories_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="categories",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="recipe.categories",
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="customer",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]