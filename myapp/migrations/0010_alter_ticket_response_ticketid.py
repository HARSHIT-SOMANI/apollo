# Generated by Django 4.0 on 2022-02-22 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_ticket_response_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_response',
            name='ticketid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ticket'),
        ),
    ]