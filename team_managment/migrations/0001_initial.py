# Generated by Django 4.0.5 on 2023-12-01 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=50)),
                ('is_adming', models.BooleanField(default=False)),
            ],
        ),
    ]
