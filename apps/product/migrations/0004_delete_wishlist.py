# Generated by Django 4.0 on 2022-01-02 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_wishlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
