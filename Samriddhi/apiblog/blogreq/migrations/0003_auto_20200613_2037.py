# Generated by Django 3.0.6 on 2020-06-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogreq', '0002_auto_20200613_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogreq',
            name='blog_id',
        ),
        migrations.AddField(
            model_name='blogreq',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
