# Generated by Django 5.0.6 on 2024-05-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthfacilities',
            name='healthcare',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
