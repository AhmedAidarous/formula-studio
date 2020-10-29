# Generated by Django 3.1.2 on 2020-10-29 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201029_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='write_off',
        ),
        migrations.AddField(
            model_name='payment',
            name='writen_off',
            field=models.BooleanField(default=False, help_text='Set whether the payment should be written off from finances'),
        ),
    ]
