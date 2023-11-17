from django.template.backends import django
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('recipe/', views.main, name='main'),
    path('recipe_category/<str:category>', views.recipe_categories, name='recipe_category'),
    path('recipe/<int:recipe_id>', views.recipe, name='recipe'),
    path('account/', views.account, name='account'),
    path('edit/<int:recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('add/', views.add_recipe, name='add_recipe'),
]