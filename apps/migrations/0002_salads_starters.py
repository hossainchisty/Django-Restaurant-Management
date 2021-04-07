# Generated by Django 3.1.4 on 2021-02-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('detail', models.TextField()),
                ('image', models.CharField(max_length=2033)),
            ],
        ),
        migrations.CreateModel(
            name='starters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('detail', models.TextField()),
                ('image', models.CharField(max_length=2033)),
            ],
        ),
    ]