# Generated by Django 3.2.4 on 2023-06-08 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]