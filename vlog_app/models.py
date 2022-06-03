from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=70,
        verbose_name='Заголовок'
    )
    img = models.ImageField(
        verbose_name='Пост',
        upload_to='photos/%Y/%m/%d'
    )
    description =models.TextField(
        verbose_name='Комментарий к посту'
    )
    is_draft = models.BooleanField(
        verbose_name='Черновик',
        default=False
    )
    is_delete = models.BooleanField(
        verbose_name='Удален',
        default=False
    )
    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        verbose_name='Дата последнего обнавления',
        auto_now=True
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Пользователь'
    )
    
    
    def __str__(self) -> str:
        return str(self.title)