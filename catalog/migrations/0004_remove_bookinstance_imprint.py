# Generated by Django 2.2.6 on 2019-11-02 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191101_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='imprint',
        ),
    ]
