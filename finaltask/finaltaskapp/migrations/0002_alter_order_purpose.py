# Generated by Django 4.2.8 on 2024-02-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finaltaskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='purpose',
            field=models.CharField(choices=[('for enquiry', 'for enquiry'), ('return', 'return'), ('place order', 'place order')], max_length=100),
        ),
    ]