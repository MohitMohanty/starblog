# Generated by Django 2.2.4 on 2020-08-07 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200807_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='datetime',
            new_name='date',
        ),
    ]
