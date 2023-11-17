from django.contrib import admin
from .models import Recipe
from django.db.models import F



class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']
    fields = ['name', 'email', 'date']
    readonly_fields = ['date']
    ordering = ['username']
    search_fields = ['email']
    search_help_text = 'Поиск по Email'


