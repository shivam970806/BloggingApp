# Generated by Django 3.0.7 on 2021-09-05 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20210905_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='blog',
            name='heading',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
