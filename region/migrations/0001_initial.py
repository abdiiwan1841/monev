# Generated by Django 2.0.4 on 2018-05-03 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'province',
                'verbose_name_plural': 'provinces',
            },
        ),
        migrations.CreateModel(
            name='Regency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.Province')),
            ],
            options={
                'verbose_name': 'regency',
                'verbose_name_plural': 'regencies',
            },
        ),
    ]
