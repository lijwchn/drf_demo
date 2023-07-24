# Generated by Django 3.2.18 on 2023-07-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='is_delete',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='creator',
            field=models.CharField(max_length=20, null=True, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='updater',
            field=models.CharField(max_length=20, null=True, verbose_name='更新人'),
        ),
    ]