# Generated by Django 3.1rc1 on 2020-09-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_auto_20200912_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='about_include',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]