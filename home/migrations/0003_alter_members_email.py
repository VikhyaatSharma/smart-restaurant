# Generated by Django 4.1.3 on 2022-11-10 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.CharField(max_length=40),
        ),
    ]
