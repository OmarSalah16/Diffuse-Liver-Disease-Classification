# Generated by Django 3.2.12 on 2022-02-19 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_report_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(upload_to='static/images/2022-02-19 02:09:54.569691'),
        ),
    ]