# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 23:42
from __future__ import unicode_literals

from django.db import migrations


def create_admin(apps, schema_editor):
    from django.conf import settings
    from django.contrib.auth.hashers import make_password
    if not settings.PRODUCTION:
        User = apps.get_model(settings.AUTH_USER_MODEL)
        admin, created = User.objects.get_or_create(username='admin')
        # User.set_password() doesn't work in migrations
        admin.password = make_password('admin')
        admin.save()


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admin)
    ]
