# Generated by Django 4.0.3 on 2022-03-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='estimated',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
