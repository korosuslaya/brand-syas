from django.contrib import admin
from .models import Category, Product
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug'] # нужно для отображения в админке 
    prepopulated_fields = {'slug' :('name', )} #поля, которые будут заполнены автоматически

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','available', 
                    'created', 'updated']
    list_filter = ['available', 'created','updated','category']#делаем возможность фильтровать в админке по этим категориям
    list_editable = ['price','available'] # делаем возможность изменения этих параметров через админку
    prepopulated_fields = {'slug' :('name', )} #поля, которые будут заполнены автоматически
