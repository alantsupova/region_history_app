from django.db import models


class Places(models.Model):
    title = models.CharField('Название места', max_length=250)
    description = models.TextField('Описание места')
    address = models.CharField('Адрес места', max_length=250)
    coordinate_x = models.DecimalField('Координата места по оси X', max_digits=7, decimal_places=5)
    coordinate_y = models.DecimalField('Координата места по оси Y', max_digits=7, decimal_places=5)
    photo = models.ImageField('Фото места')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Routes(models.Model):
    title = models.CharField('Название маршрута', max_length=250)
    places = models.ManyToManyField(Places, related_name='routes')
    time = models.CharField('Время прогулки', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
