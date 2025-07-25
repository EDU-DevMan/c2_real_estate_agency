from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    owner_pure_phone = PhoneNumberField('Нормализованный номер владельца',
                                        max_length=20, blank=True, null=True)
    new_building = models.BooleanField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона',
                                      null=True,
                                      blank=True,
                                      db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    liked_by = models.ManyToManyField(User,
                                      verbose_name='Кто лайкнул:',
                                      related_name="liked_posts",
                                      blank=True, null=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    username = models.ForeignKey(User,
                                 verbose_name='Кто жаловался:',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)
    flat = models.ForeignKey(
        Flat,
        verbose_name='Квартира, на которую пожаловались:',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    complaint = models.TextField('Текст жалобы:',
                                 null=True, 
                                 blank=True)

    def __str__(self):
        return f'{self.username}, {self.flat}, ({self.complaint})'


class Owner(models.Model):
    owner = models.CharField('ФИО владельца:', max_length=200)
    owners_phonenumber = models.CharField('Номер владельца:',
                                          blank=True, null=True, max_length=20)
    owner_pure_phone = PhoneNumberField('Нормализованный номер владельца:',
                                        max_length=20, blank=True, null=True)
    apartments_owned = models.ManyToManyField(
        Flat,
        verbose_name='Квартиры в собственности:',
        related_name='owners',
        blank=True, null=True,
        db_index=True)

    def __str__(self):
        return f'{self.owner}'
