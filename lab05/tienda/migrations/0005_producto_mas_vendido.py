# Generated by Django 4.2.5 on 2023-10-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_cliente_es_vip'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='mas_vendido',
            field=models.BooleanField(default=False),
        ),
    ]
