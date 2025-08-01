# Generated by Django 5.2.4 on 2025-07-23 07:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_rename_complaintaboutflat_complaint'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complaint',
            field=models.TextField(blank=True, null=True, verbose_name='Текст жалобы:'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.flat', verbose_name='Квартира, на которую пожаловались:'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался:'),
        ),
    ]
