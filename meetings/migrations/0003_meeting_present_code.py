# Generated by Django 2.2.5 on 2019-10-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20191008_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='present_code',
            field=models.TextField(default='asd'),
            preserve_default=False,
        ),
    ]