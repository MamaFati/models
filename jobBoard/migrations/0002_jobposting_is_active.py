# Generated by Django 5.0.6 on 2024-05-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobBoard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
