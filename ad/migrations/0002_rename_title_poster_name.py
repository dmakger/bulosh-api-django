# Generated by Django 4.1 on 2024-04-21 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poster',
            old_name='title',
            new_name='name',
        ),
    ]