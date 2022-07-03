from urllib import request

import pytz
from django.conf import settings
from django.core.exceptions import ValidationError
# from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from trip.validators import validator_datetime
from users.models import User


class Company(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='Компания',
        help_text='Введите название компании'
        )
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name    
    
class Plane(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='Название самолета',
        help_text='Введите название самолета'
    )
    number = models.PositiveIntegerField(
        verbose_name='Номер самолета',
        help_text='Введите номер самолета'
    )
    ready = models.BooleanField(
        default=False,
        verbose_name='Готовность самолета',
        help_text='Измените готовность самолета'
    )
    capacity = models.PositiveIntegerField(
        verbose_name='Количество мест',
        help_text='Введите кол-во мест в самолете'
    )
    class Meta:
        verbose_name = 'Самолет'
        verbose_name_plural = 'Самолеты'

    def __str__(self):
        return self.name

class Airport(models.Model):
    TZ_CHOICES = [
            ("UTC" , "UTC"),
            ("Europe/Moscow" , "Europe/Moscow"),
            ("Asia/Kamchatka", "Asia/Kamchatka")
        ]
    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='Название аэропорта',
        help_text='Введите название аэропорта'
    )
    ap_time_zone = models.CharField(
        max_length=128,
        verbose_name='Таймзона аэропорта',
        help_text='Введите таймзону аэропорта',
        choices=TZ_CHOICES,
        default=settings.TIME_ZONE
        )
    
    class Meta:
        verbose_name = 'Аэропорт'
        verbose_name_plural = 'Аэропорты'

    def __str__(self):
        return self.name

class Trip(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='trips',
        verbose_name='Компания',
        help_text='Компания'
    )
    plane = models.ForeignKey(
        Plane,
        on_delete=models.CASCADE,
        related_name='trips',
        verbose_name='Самолет',
        help_text='Самолет'
    )
    airport_from = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name='trips_from',
        verbose_name='Из аэропорта',
        help_text='Из аэропорта'
    )
    airport_to = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name='trips_to',
        verbose_name='В аэропорт',
        help_text='В аэропорт'
    )
    time_out = models.DateTimeField(
        validators=[validator_datetime,],
        verbose_name='Дата/Время вылета',
    )
    time_in = models.DateTimeField(
        verbose_name='Дата/Время прилета',
        validators=[validator_datetime,],
    )
    class Meta:
        verbose_name = 'Перелет'   
        verbose_name_plural = 'Перелеты'

    def __str__(self):
        return f'id: {self.id}, по маршруту: {self.airport_from} - {self.airport_to}, вылет {self.time_out}, прибытие {self.time_in}'

    def clean(self):
        board_buse = self.plane.trips.all().aggregate(models.Max('time_in'))
        if self.time_out <= board_buse['time_in__max']:
            raise ValidationError('В это время самолет еще в полете.')
    

class Pass_in_trip(models.Model):
    passenger = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pass_in_trip',
        verbose_name='Пассажир',
        help_text='Пассажир'
    )
    place = models.PositiveIntegerField(
        unique=True,
        verbose_name='Номер места',
        help_text='Введите номер места',
        # validators=[MinValueValidator(1, 'Место не может быть менее 1.'),]
    )
    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name='pass_in_trips',
        verbose_name='Пассажиры в рейсе',
        help_text='Пассажиры в рейсе',
    )

    class Meta:
        verbose_name = 'Пассажир_место'
        verbose_name_plural = 'Пассажиры_места'
    
    def __str__(self):
        return f'Пассажир - {self.passenger.first_name} {self.passenger.last_name} место - {self.place} рейс ID -{self.trip.id}'

    def clean(self):
        if self.place > self.trip.plane.capacity:
            raise ValidationError('Место не может быть больше, чем мест в самолете.')
