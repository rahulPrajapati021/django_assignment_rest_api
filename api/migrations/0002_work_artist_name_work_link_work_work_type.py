# Generated by Django 4.2 on 2023-05-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='artist_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='link',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='work_type',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
