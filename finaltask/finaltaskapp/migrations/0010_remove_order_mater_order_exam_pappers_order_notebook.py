# Generated by Django 4.2.8 on 2024-03-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finaltaskapp', '0009_alter_order_address_alter_order_deptname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='mater',
        ),
        migrations.AddField(
            model_name='order',
            name='exam_pappers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='notebook',
            field=models.BooleanField(default=False),
        ),
    ]
