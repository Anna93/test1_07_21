# Generated by Django 3.1.5 on 2021-01-09 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='User name')),
                ('password', models.CharField(max_length=10, verbose_name='Password')),
                ('email', models.CharField(max_length=20, verbose_name='Email')),
            ],
        ),
    ]
