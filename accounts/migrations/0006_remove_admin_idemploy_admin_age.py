# Generated by Django 5.0.1 on 2024-01-09 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_idempoy_admin_idemploy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='idEmploy',
        ),
        migrations.AddField(
            model_name='admin',
            name='age',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
    ]
