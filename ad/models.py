from django.db import models


# Постеры
class Poster(models.Model):
    name = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    link = models.CharField('Ссылка', max_length=128)
    wallpaper = models.ImageField('Обои', upload_to="media/poster/")
    is_visible = models.BooleanField('Показывается ли', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = "Постер"
        verbose_name_plural = "Постеры"

    def __str__(self):
        return self.name
