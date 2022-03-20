# Generated by Django 4.0.3 on 2022-03-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=1000)),
                ('user', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('observations', models.TextField(blank=True, default='')),
            ],
        ),
    ]