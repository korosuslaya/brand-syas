from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)#db_index=True - используется, если нужно часть фильтровать эти данные.
    slug = models.SlugField(max_length=100, unique=True)#создает url(понятный url). Нр: если name = "Nike Air Max", то slug = "nike-air-max".
    
    class Meta:
        ordering = ('name',)# — по умолчанию сортировать категории по имени.
        verbose_name = 'Категория' # — человекочитаемое имя модели в админке Django (ед. число).
        verbose_name_plural = 'Категории'# — то же, но во множественном числе.
    
    # Этот метод определяет, что будет отображаться при выводе объекта в админке или при print(obj).
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products', 
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique = 100)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    descruption = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   

    class Meta: 
        ordering = ('name', )
        verbose_name = 'Продукт' # — человекочитаемое имя модели в админке Django (ед. число).
        verbose_name_plural = 'Продукты'# — то же, но во множественном числе.

    def __str__(self):
        return self.name
    
class ProductSize(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ]

    product = models.ForeignKey(Product, related_name='sizes', on_delete=models.CASCADE)
    size = models.CharField(max_length=4, choices=SIZE_CHOICES)
    stock = models.PositiveIntegerField(default=0)  # количество товара в наличии для этого размера
    available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('product', 'size')

    def __str__(self):
        return f"{self.product.name} — {self.size}"
