# Generated by Django 2.2.16 on 2022-10-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20221011_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(error_messages={'blank': 'Password cannot be empty.', 'min_length': 'Password too short.', 'required': 'Салапумбалашка.'}),
        ),
    ]
