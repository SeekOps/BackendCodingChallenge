# Generated by Django 3.1.3 on 2022-02-14 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='preferences',
            field=models.CharField(max_length=128, null=True),
        ),
    ]