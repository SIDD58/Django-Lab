# Generated by Django 5.0.1 on 2024-02-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0005_groupmember'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupmember',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_features',
            field=models.CharField(choices=[('Cruise', 'Cruise'), ('Control', 'Control'), ('Audio', 'Audio'), ('Interface', 'Interface'), ('Airbags', 'Airbags'), ('Air', 'Air'), ('Conditioning', 'Conditioning'), ('Seat', 'Seat'), ('Heating', 'Heating'), ('ParkAssist', 'ParkAssist'), ('Power', 'Power'), ('Steering', 'Steering'), ('Reversing', 'Reversing'), ('Camera', 'Camera'), ('Auto', 'Auto'), ('Start / Stop', 'Start / Stop')], default='Seat', max_length=100),
        ),
    ]