# Generated by Django 4.1.4 on 2023-02-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_communitymodel_table_alter_rewardsmodel_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapp',
            name='appID',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userapp',
            name='userProg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userapp',
            name='userStatus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user_phonenumber2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
