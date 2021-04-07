# Generated by Django 3.1.7 on 2021-04-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefs',
            name='facebook',
            field=models.URLField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='instagram',
            field=models.URLField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='linkedin',
            field=models.URLField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='twitter',
            field=models.URLField(blank=True, max_length=3000, null=True),
        ),
    ]