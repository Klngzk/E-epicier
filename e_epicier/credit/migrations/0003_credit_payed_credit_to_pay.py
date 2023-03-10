# Generated by Django 4.1.5 on 2023-02-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0002_qnt_produit_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='payed',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='credit',
            name='to_pay',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
