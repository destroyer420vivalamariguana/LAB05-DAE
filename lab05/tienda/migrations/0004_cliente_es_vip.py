# Generated by Django 4.2.5 on 2023-10-01 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='es_vip',
            field=models.BooleanField(default=False),
        ),
    ]
