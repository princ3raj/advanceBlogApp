# Generated by Django 3.1 on 2020-08-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninorooms', '0002_auto_20200819_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninorooms',
            name='pg_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
