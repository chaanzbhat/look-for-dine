# Generated by Django 3.0.4 on 2020-04-16 17:04

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_auto_20200404_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='recommendation',
            field=jsonfield.fields.JSONField(default=[]),
            preserve_default=False,
        ),
    ]
