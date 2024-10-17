from datetime import datetime

from django.db import models

from config import settings


class Category(models.Model):
    '''Создаем модель категории товаров'''
    name = models.CharField(
        max_length=50,
        verbose_name="наименование",
        help_text="введите наименование категории",
    )
    description = models.CharField(
        max_length=200, verbose_name="описание", help_text="введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    '''Модель продукта'''
    name = models.CharField(
        max_length=50,
        verbose_name="наименование продукта",
        help_text="введите наименование продукта",
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=150, verbose_name="описание", help_text="опишите продукта"
    )
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        help_text="загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="категория",
        help_text="введите название категории",
        related_name="product",
    )
    price = models.IntegerField(
        verbose_name="стоимость", help_text="стоимость продукта"
    )
    created_at = models.DateField(default=datetime.now, verbose_name="дата создания")
    updated_at = models.DateField(default=datetime.now, verbose_name="дата редактирования")
    views_counter = models.PositiveIntegerField(default=0, verbose_name='просмотры')

    def get_active_version(self):
        return self.versions.filter(is_current=True).first()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price", "created_at", "updated_at"]
        permissions = [
            ('can_edit_description', 'Can edit description'),
            ('can_edit_category', 'Can edit category'),
            ('set_published', 'Can publish product'),
        ]

    def __str__(self):
        return f"{self.name}"


class Version(models.Model):
    '''Модель версии продукта'''
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        help_text="Выберите продукт, к которому относится версия",
        related_name="versions"
    )
    version_number = models.SmallIntegerField(
        verbose_name="Номер версии",
        help_text="Введите номер версии"
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии"
    )
    is_current = models.BooleanField(
        default=True,
        verbose_name="Текущая версия",
        help_text="Установите, если это текущая версия продукта"
    )

    def save(self, *args, **kwargs):
        # Если номер версии не установлен, получаем максимальный номер версии для продукта
        if not self.version_number:
            max_version = Version.objects.filter(product=self.product).aggregate(models.Max('version_number'))[
                'version_number__max']
            self.version_number = (max_version + 1) if max_version is not None else 1

        # Устанавливаем флаг is_current для всех предыдущих версий в False
        Version.objects.filter(product=self.product, is_current=True).update(is_current=False)

        # Устанавливаем текущую версию как актуальную
        self.is_current = True

        # Сохраняем версию
        super().save(*args, **kwargs)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["-is_current", "version_number"]
        constraints = [
            models.UniqueConstraint(fields=['product', 'version_number'], name='unique_product_version')
        ]

    def __str__(self):
        return f"{self.version_name} (Версия {self.version_number})"
