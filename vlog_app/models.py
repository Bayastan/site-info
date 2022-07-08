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
    
    
class Contact(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название контакта",
    )
    
    contact_url = models.URLField(
        verbose_name="Ссылка на контакт",
        unique=True
    )
    
    create_date = models.DateTimeField(
        verbose_name="Дата создания контакта",
        auto_now_add=True
        
    )
    
    update_date = models.DateTimeField(
        verbose_name="Дата последнего обновления контакта",
        auto_now=True
    )
    
    is_active = models.BooleanField(
        verbose_name="Активный",
        default=True
    )
    
    class Meta:
        unique_together = ("name", "contact_url")
        
    def test(self):
        return 2 + 2

    def __str__(self) -> str:
        return str(self.name)
    
    
class SiteInfo(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="Название сайта"
    )
    
    title = models.CharField(
        max_length=20,
        verbose_name="Заголовок сайта"
    )
    
    description = models.CharField(
        max_length=500,
        verbose_name="Описание сайта",
    )
    
    create_date = models.DateTimeField(
        verbose_name="Дата создания сайта",
        auto_now_add=True,
    )
    
    update_date = models.DateTimeField(
        verbose_name="Дата последнего обновления контакта",
        auto_now=True
    )
    
    is_active = models.BooleanField(
        verbose_name="Активный",
        default=True
    )
        
    class Meta:
        ordering = ("create_date",)
    
    def __str__(self) -> str:
        return str(self.name)
    
    