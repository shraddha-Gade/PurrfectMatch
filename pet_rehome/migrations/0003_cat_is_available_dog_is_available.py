# Generated by Django 5.0.1 on 2024-02-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_rehome', '0002_cat_dog_delete_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
