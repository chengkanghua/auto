# Generated by Django 3.2.5 on 2021-07-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=1, verbose_name='年龄'),
            preserve_default=False,
        ),
    ]
