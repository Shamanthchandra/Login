# Generated by Django 2.1.4 on 2019-01-08 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
