# Generated by Django 4.1.3 on 2022-11-11 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_issued'),
    ]

    operations = [
        migrations.AddField(
            model_name='issued',
            name='charged',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
