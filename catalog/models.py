from django.db import models

class Category(models.Model):
    name = models.CharField(max_length='50', verbose_name='наименование', help_text='введите наименование категории')
    description = models.CharField(max_length='50', verbose_name='описание', help_text='введите описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        pass

class Product(models.Model):
    name = models.CharField(max_length='50', verbose_name='наименование продукта', help_text='введите наименование продукта')
    description = models.CharField(max_length='150', verbose_name='описание', help_text='опишите продукта')
    image = models.ImageField(upload_to='products/', blank=True, null=True,help_text='загрузите изображение продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(max_length='10',verbose_name='стоимость', help_text='стоимость продукта')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='дата создания')
    updated_at =models.DateTimeField(verbose_name='дата редактирования')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'price', 'create_date', 'edit_date']

    def __str__(self):
        return f'{self.name}'





