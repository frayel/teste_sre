# Generated by Django 3.2.6 on 2021-08-20 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PendingPaymentModel',
        ),
    ]