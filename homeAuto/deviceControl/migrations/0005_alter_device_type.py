# Generated by Django 4.2.16 on 2024-10-10 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deviceControl', '0004_devicetype_location_room_alter_device_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deviceControl.devicetype'),
        ),
    ]
