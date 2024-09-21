from datetime import datetime


from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
        help_text="введите название поста",
    )
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    context = models.TextField()
    image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True,
        help_text="загрузите изображение поста", )
    created_at = models.DateField(default=datetime.now, verbose_name="дата создания поста")
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_counter = models.PositiveIntegerField(default=0, verbose_name='просмотры')

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["title", "created_at", "views_counter"]

    def __str__(self):
        return f"{self.title}"
