# Generated by Django 4.0 on 2022-02-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_ticket_date_ticket_date2_ticket_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='date2',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.CharField(max_length=500),
        ),
    ]
