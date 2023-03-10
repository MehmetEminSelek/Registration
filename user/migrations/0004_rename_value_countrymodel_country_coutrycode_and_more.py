# Generated by Django 4.1.4 on 2023-02-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_userapp_appid_alter_userapp_userprog_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countrymodel',
            old_name='value',
            new_name='country_coutrycode',
        ),
        migrations.AddField(
            model_name='countrymodel',
            name='country_countryname',
            field=models.CharField(default=12, max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='countrymodel',
            name='country_phoneprefix',
            field=models.CharField(default=49, max_length=4),
            preserve_default=False,
        ),
    ]
