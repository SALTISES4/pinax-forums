# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-16 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_forums', '0004_forumthread_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumreply',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinax_forums.ForumReply'),
        ),
    ]
