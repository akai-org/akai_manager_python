# Generated by Django 2.2.5 on 2019-10-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='code',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6),
        ),
    ]
