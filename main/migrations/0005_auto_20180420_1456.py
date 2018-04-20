# Generated by Django 2.0.4 on 2018-04-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180417_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='instrument',
            field=models.CharField(choices=[('0', 'Instrument A'), ('1', 'Instrument B'), ('2', 'Instrument C')], max_length=2),
        ),
        migrations.AlterUniqueTogether(
            name='questionnaire',
            unique_together={('diklat', 'instrument')},
        ),
    ]
