# Generated by Django 4.2.16 on 2024-10-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_alter_portfoliomodel_framework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomodel',
            name='framework',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]