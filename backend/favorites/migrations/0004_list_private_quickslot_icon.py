# Generated by Django 5.0.6 on 2024-07-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0003_remove_mypin_user_list_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='quickslot',
            name='icon',
            field=models.IntegerField(default=1),
        ),
    ]