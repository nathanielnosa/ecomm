# Generated by Django 4.0.4 on 2022-04-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_order_payment_completed_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Paystack', 'Paystack'), ('Payment Transfer', 'Payment Transfer')], default='Cash On Delivery', max_length=20),
        ),
    ]
