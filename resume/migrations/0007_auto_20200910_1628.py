# Generated by Django 3.1rc1 on 2020-09-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_social_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
