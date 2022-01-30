# Generated by Django 3.2.5 on 2022-01-30 21:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20220125_0742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('discountType', models.CharField(default='FTB2022', max_length=200)),
                ('discountActive', models.BooleanField(default=False)),
                ('startDate', models.DateTimeField()),
                ('stopDate', models.DateTimeField()),
                ('ftbDiscountBalance', models.DecimalField(decimal_places=2, default=4.5, max_digits=5)),
                ('wafDiscountBalance', models.DecimalField(decimal_places=2, default=4.5, max_digits=5)),
                ('frbDiscountBalance', models.DecimalField(decimal_places=2, default=4.5, max_digits=5)),
                ('lysDiscountBalance', models.DecimalField(decimal_places=2, default=4.5, max_digits=5)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order')),
            ],
        ),
    ]
