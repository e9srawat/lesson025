# Generated by Django 4.2.9 on 2024-01-14 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_mobile_number1_contact_mobile_number1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]