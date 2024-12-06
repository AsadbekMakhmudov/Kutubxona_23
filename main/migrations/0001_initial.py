# Generated by Django 5.1.2 on 2024-12-02 11:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kutubxonachi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('telefon_raqam', models.CharField(max_length=15)),
                ('ish_vaqti', models.CharField(choices=[('08:00-13:00', '08:00-13:00'), ('13:00-18:00', '13:00-18:00'), ('18:00-23:00', '18:00-23:00')], max_length=55)),
            ],
            options={
                'verbose_name': 'Kutubxonachi',
                'verbose_name_plural': 'Kutubxonachilar',
            },
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('t_yil', models.DateField(blank=True, null=True)),
                ('jins', models.CharField(choices=[('erkak', 'erkak'), ('ayol', 'ayol')], max_length=10)),
                ('millat', models.CharField(blank=True, max_length=50, null=True)),
                ('tirik', models.BooleanField(default=False)),
                ('kitob_soni', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Muallif',
                'verbose_name_plural': 'Mualliflar',
            },
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('yosh', models.PositiveSmallIntegerField()),
                ('telefon_raqam', models.CharField(max_length=15)),
                ('guruh', models.CharField(max_length=255)),
                ('kurs', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
            ],
            options={
                'verbose_name': 'Talaba',
                'verbose_name_plural': 'Talabalar',
            },
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('janr', models.CharField(max_length=50)),
                ('sahifa', models.PositiveSmallIntegerField()),
                ('muqova', models.CharField(choices=[('Qattiq', 'Qattiq'), ('Yumshoq', 'Yumshoq')], max_length=50)),
                ('muallif', models.ManyToManyField(to='main.muallif')),
            ],
            options={
                'verbose_name': 'Kitob',
                'verbose_name_plural': 'Kitoblar',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olingan_sana', models.DateTimeField(blank=True, null=True)),
                ('qaytargan_sana', models.DateTimeField(blank=True, null=True)),
                ('qaytardi', models.BooleanField(default=False)),
                ('kitob', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.kitob')),
                ('kutubxonachi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.kutubxonachi')),
                ('talaba', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.talaba')),
            ],
            options={
                'verbose_name': 'Rekord',
                'verbose_name_plural': 'Rekordlar',
            },
        ),
    ]
