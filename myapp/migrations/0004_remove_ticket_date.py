# Generated by Django 4.0 on 2022-02-21 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_ticket_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='date',
        ),
    ]
