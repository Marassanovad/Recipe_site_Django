from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import RecipeForm, LogIn, UserRegistrationForm
from .models import Recipe, Categories


# import logging
# from datetime import datetime
#
# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO, filename="./logs/lesson1.log", filemode='a', format='%(levelname)s %(message)s')
# Create your views here.

def main(request):
    recipes = Recipe.objects.all().order_by("?")
    # logger.info('Пользователь успешно зашел: ' + str(datetime.now()))
    return render(request, "recipes.html", {"Recipes": recipes[:9]})


def recipe_categories(request, category):
    # logger.info('Пользователь успешно зашел: ' + str(datetime.now()))
    category = get_object_or_404(Categories, name=category)
    recipes = Recipe.objects.filter(categories=category.id)
    return render(request, "recipes.html", {"Recipes": recipes[:9]})

def recipe(request, recipe_id):
    # logger.info('Пользователь успешно зашел: ' + str(datetime.now()))
    recipes = Recipe.objects.filter(pk=recipe_id).first()
    return render(request, "recipe.html", {"Recipes": recipes})

def edit_recipe(request, recipe_id):
    # logger.info('Пользователь успешно зашел: ' + str(datetime.datetime.now()))
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        if recipe.customer == request.user:
            if form.is_valid():
                datas = {"categories": form.cleaned_data['categories'], "title": form.cleaned_data['title'], "products": form.cleaned_data['products'], "description": form.cleaned_data['description'], "cooking_steps": form.cleaned_data['cooking_steps'], "cooking_time": form.cleaned_data['cooking_time'], "image": form.cleaned_data['image']}
                recipe = get_object_or_404(Recipe, pk=recipe_id)
                for data in datas:
                    if datas[data] != "" and data == "title":
                        recipe.title = datas[data]
                    elif datas[data] != "" and data == "description":
                        recipe.description = datas[data]
                    elif datas[data] != "" and data == "categories":
                        category = datas[data]
                    elif datas[data] != "" and data == "products":
                        recipe.products = datas[data]
                    elif datas[data] != "" and data == "cooking_steps":
                        recipe.cooking_steps = datas[data]
                    elif datas[data] != "" and data == "cooking_time":
                        recipe.cooking_time = datas[data]
                    elif datas[data] != "" and data == "image":
                        image = datas[data]
                        fs = FileSystemStorage()
                        fs.save(image.name, image)
                        recipe.image = image.name
                    categories = get_object_or_404(Categories, name=category)
                    recipe.categories = categories
                    recipe.save()
                message = 'Рецепт обновлен'
            return render(request, 'edit_recipe.html', {'form': form, 'message': message})
        else:
            message = 'Это не ваш рецепт. Ничего не выйдет'
            return render(request, 'edit_recipe.html', {'form': form, 'message': message})
    else:
        form = RecipeForm()
        message = 'Заполните форму'
        return render(request, 'edit_recipe.html', {'form': form, 'message': message})

def add_recipe(request):
    title = 'Добавить рецепт'
    head_title = 'Добавить рецепт: '
    cooking_form = RecipeForm(request.POST, request.FILES)
    if request.method == 'GET':
        return render(request, 'add_recipe.html',
                      {'form': cooking_form,
                       'title': title,
                       'head_title': head_title,
                       'button': f'Add_recipe',})
    elif request.method == 'POST':
        if cooking_form.is_valid():
            name = cooking_form.cleaned_data['title']
            category = cooking_form.cleaned_data['categories']
            products = cooking_form.cleaned_data['products']
            description = cooking_form.cleaned_data['description']
            steps = cooking_form.cleaned_data['cooking_steps']
            cooking_time = cooking_form.cleaned_data['cooking_time']
            image = cooking_form.cleaned_data['image']
            recipe = Recipe(title=name, description=description,products=products, cooking_steps=steps, cooking_time=cooking_time, image=image)
            category = get_object_or_404(Categories, name=category)
            # fs = FileSystemStorage()
            # fs.save(image.name, image)
            # print(image.name)
            # recipe.image = image.name
            recipe.customer = request.user
            recipe.categories= category
            recipe.save()

            messages.success(request, f'Рецепт сохранен. {request.user}')
            return redirect('main')
    else:
        messages.error(request, f'Не получилось сохранить рецепт. {request.user}')
        return render(request, 'add_recipe.html',
                      {'form': cooking_form,
                       'title': title,
                       'head_title': head_title})
    return render(request, 'add_recipe.html',
                  {'form': cooking_form,
                   'title': title,
                   'head_title': head_title,
                   'button': f'Add_recipe',})
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = 'Authenticated successfully'
                    return redirect(account)
                else:
                    message = 'Disabled account'
                    return render(request, 'login.html', {'form': form, 'message': message})
            else:
                message = 'Invalid login'
                return render(request, 'login.html', {'form': form, 'message': message})
    else:
        form = LogIn()
        message = 'Заполните форму'
    return render(request, 'login.html', {'form': form, 'message': message, 'button': 'Login'})

def user_logout(request):
    logout(request)
    return redirect(user_login)

def register(request):
    title = 'Регистрация'
    if request.method == 'POST':
        message = 'Ошибка в данных'
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, f'Пользователь сохранен. Можете авторизоваться')
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        message = 'Заполните форму'
    return render(request, 'account_reg.html', {'user_form': user_form, 'title': title,'message': message, 'button': 'Register'})

@login_required
def account(request):
    user = get_object_or_404(User, username=request.user)
    recipe = Recipe.objects.filter(customer=user.id).order_by("-id")
    return render(request, 'account.html', {"Recipes": recipe[:9]})

