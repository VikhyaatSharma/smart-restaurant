# Generated by Django 4.1.3 on 2023-05-04 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_tokens_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
