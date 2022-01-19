# Generated by Django 4.0.1 on 2022-01-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='modified',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]