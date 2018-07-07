# Generated by Django 2.0.6 on 2018-07-05 23:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import status.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=160, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=status.models.upload_status_image)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
