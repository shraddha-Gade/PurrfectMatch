# Generated by Django 5.0.1 on 2024-02-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0003_rename_name_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='contact_no',
            field=models.CharField(),
        ),
    ]
