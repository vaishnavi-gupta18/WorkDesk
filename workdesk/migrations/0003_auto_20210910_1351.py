# Generated by Django 3.2.6 on 2021-09-10 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workdesk', '0002_auto_20210908_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='card_creator', to='workdesk.member'),
        ),
        migrations.AlterField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_creator', to='workdesk.member'),
        ),
    ]
