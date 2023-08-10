from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, default=1)
    image = models.ImageField("Изображение", upload_to='photos/%Y/%m/%d/', default='', blank=True)

    # from app_advertisements.models import Advertisement
    # Advertisement.objects.all()
    # exit()

    class Meta:
        db_table = "advertisement"
        verbose_name = "объявление"
        verbose_name_plural = "объявления"

    def __str__(self):
        return f'(id={self.id}, title={self.title}, price={self.price})'

