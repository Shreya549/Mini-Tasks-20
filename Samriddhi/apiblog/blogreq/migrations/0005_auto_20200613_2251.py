# Generated by Django 3.0.6 on 2020-06-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogreq', '0004_auto_20200613_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogreq',
            name='date_rec',
            field=models.DateField(auto_now_add=True),
        ),
    ]