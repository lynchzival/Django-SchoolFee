# Generated by Django 3.2.13 on 2022-06-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20220618_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
