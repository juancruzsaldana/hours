# Generated by Django 4.0.3 on 2022-03-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='access',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='access',
            name='user',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
