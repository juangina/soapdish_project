# Generated by Django 3.2.5 on 2021-10-13 13:22

from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0004_alter_bar_photo_main'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='bar_soap',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=models.SET(inventory.models.get_deleted_bar), to='bars.bar'),
        ),
    ]