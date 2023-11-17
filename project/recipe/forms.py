from enum import Enum

from django import forms
from .models import Categories
from django.contrib.auth.models import User


# class Register(forms.Form):
#     username = forms.CharField(max_length=10)
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
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
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)
        labels = {'username': 'Имя пользователя'}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    # class Meta:
    #     model = Author
    #     fields = ('username', 'email')


class LogIn(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)



class RecipeForm(forms.Form):
    categories = forms.CharField(label='Категория', required=False, widget=forms.Select(attrs={'required': 'True'}, choices=CATEGORY_CHOICE))
    title = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))
    products =forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите продукты'}))
    description = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}))
    cooking_steps = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}))
    cooking_time = forms.IntegerField(min_value=10, required=False, step_size=5)
    image = forms.ImageField(required=False)



