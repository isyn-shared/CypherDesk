# Generated by Django 2.0.6 on 2018-06-29 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsrecord',
            old_name='data',
            new_name='date',
        ),
    ]