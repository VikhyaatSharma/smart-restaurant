# Generated by Django 4.1.3 on 2022-11-10 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_members_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=20)),
                ('charge', models.CharField(max_length=5)),
            ],
        ),
    ]