# Generated by Django 2.0.6 on 2018-06-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('short_news', models.CharField(max_length=128)),
                ('news', models.TextField()),
                ('data', models.DateTimeField()),
            ],
        ),
    ]