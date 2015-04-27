# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todoitem_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='due',
            field=models.DateTimeField(null=True, verbose_name='Due Date', blank=True),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date', null=True),
        ),
    ]
