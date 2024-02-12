# Generated by Django 5.0.1 on 2024-02-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('contact_no', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
