# Generated by Django 4.2.16 on 2024-10-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_portfoliomodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomodel',
            name='framework',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='language',
            field=models.CharField(max_length=200, null=True),
        ),
    ]