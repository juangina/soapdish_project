# Generated by Django 3.2.5 on 2021-07-29 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listing',
            new_name='bar',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='listing_id',
            new_name='bar_id',
        ),
    ]