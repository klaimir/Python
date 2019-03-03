# Generated by Django 2.1.3 on 2019-03-03 11:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('intro', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('image', models.FileField(upload_to='')),
                ('status', models.CharField(choices=[('PUB', 'Published'), ('Pending', 'Pending')], default='PUB', max_length=3)),
                ('publication_date', models.DateTimeField(default=datetime.datetime.now)),
                ('last_modification', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='categories.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]