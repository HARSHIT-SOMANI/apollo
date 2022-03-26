# Generated by Django 4.0 on 2022-02-22 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_ticket_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticket_response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=500)),
                ('ticketid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.ticket')),
            ],
        ),
    ]