# Generated by Django 5.1.3 on 2025-01-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]
