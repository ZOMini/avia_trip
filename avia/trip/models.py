from django.db import models
from pyexpat import model

from users.models import User


class Company(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Компания',
        help_text='Введите название компании'
        )
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Pass_in_trip(models.Model):
    passenger = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name='Пассажир',
        help_text='Пассажир'
    )
    place = models.SmallIntegerField(
        max_length=3,
        verbose_name='Номер места',
        help_text='Введите номер места'
    )
    class Meta:
        verbose_name = 'Пассажир_место'
        verbose_name_plural = 'Пассажиры_места'
    
class Plane(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Название самолета',
        help_text='Введите название самолета'
    )
    number = models.SmallIntegerField(
        max_length=12,
        verbose_name='Номер самолета',
        help_text='Введите номер самолета'
    )
    ready = models.BooleanField(
        default=False,
        verbose_name='Готовность самолета',
        help_text='Измените готовность самолета'
    )
    capacity = models.SmallIntegerField(
        max_length=3,
        verbose_name='Количество мест',
        help_text='Введите кол-во мест в самолете'
    )
    class Meta:
        verbose_name = 'Самолет'
        verbose_name_plural = 'Самолеты'

class Airport(models.model):
    name = models.CharField(
        max_length=128,
        verbose_name='Название аэропорта',
        help_text='Введите название аэропорта'
    )
    class Meta:
        verbose_name = 'Аэропорт'
        verbose_name_plural = 'Аэропорты'

class Trip(model.Model):
    company = models.ManyToManyField(
        Company,
        on_delete=models.CASCADE,
        related_name='trips',
        verbose_name='Компания',
        help_text='Компания'
    )
    plane = models.ManyToManyField(
        Plane,
        on_delete=models.CASCADE,
        related_name='trips',
        verbose_name='Самолет',
        help_text='Самолет'
    )
    airport_from = models.ManyToManyField(
        Airport,
        on_delete=models.CASCADE,
        related_name='trips',
        verbose_name='Из аэропорта',
        help_text='Из аэропорта'
    )
    airport_to = models.ManyToManyField(
        Airport,
        on_delete=models.CASCADE,
        related_name='trips',
        verbose_name='В аэропорт',
        help_text='В аэропорт'
    )
    time_out = models.DateTimeField(
        verbose_name='Дата/Время вылета',
    )
    time_in = models.DateTimeField(
        verbose_name='Дата/Время прилета',
    )
    class Meta:
        verbose_name = 'Перелет'   
        verbose_name_plural = 'Перелеты'
