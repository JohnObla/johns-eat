# Generated by Django 3.1 on 2020-08-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20200825_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
