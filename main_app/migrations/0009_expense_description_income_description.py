# Generated by Django 4.2.3 on 2023-08-05 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_budget_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='description',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
