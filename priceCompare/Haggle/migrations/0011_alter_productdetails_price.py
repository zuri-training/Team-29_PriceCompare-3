# Generated by Django 4.0.6 on 2022-08-11 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Haggle', '0010_remove_productdetails_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='price',
            field=models.IntegerField(),
        ),
    ]
