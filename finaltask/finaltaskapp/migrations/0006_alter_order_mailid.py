# Generated by Django 4.2.8 on 2024-03-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finaltaskapp', '0005_alter_order_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mailid',
            field=models.EmailField(max_length=254),
        ),
    ]