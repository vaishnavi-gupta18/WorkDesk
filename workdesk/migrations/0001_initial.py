# Generated by Django 3.2.6 on 2021-09-03 16:08

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('start_date', models.DateTimeField()),
                ('creator', models.CharField(max_length=12)),
                ('status', models.CharField(max_length=100)),
                ('is_public', models.BooleanField()),
                ('members', models.ManyToManyField(to='workdesk.Member')),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workdesk.project')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('start_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('creator', models.CharField(max_length=12)),
                ('assignees', models.ManyToManyField(to='workdesk.Member')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workdesk.list')),
            ],
        ),
    ]
