# Generated by Django 3.0.4 on 2020-04-04 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_customer_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='profile_pic',
            new_name='email',
        ),
    ]
