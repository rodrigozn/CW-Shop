# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 17:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20160218_0812'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartline',
            old_name='product',
            new_name='variant',
        ),
        migrations.AlterUniqueTogether(
            name='cartline',
            unique_together=set([('cart', 'variant', 'data')]),
        ),
    ]
