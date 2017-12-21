# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='role',
            name='title',
        ),
        migrations.AddField(
            model_name='role',
            name='name',
            field=models.CharField(default='a', max_length=32, verbose_name='角色名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=32, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='roles',
            field=models.ManyToManyField(to='app02.Role', verbose_name='担任的角色'),
        ),
    ]
