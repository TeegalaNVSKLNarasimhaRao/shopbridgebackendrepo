# Generated by Django 3.1.6 on 2021-02-05 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='productImage',
        ),
    ]
