# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(default='None', max_length=4000)),
                ('effect', models.CharField(default='None', max_length=4000)),
                ('homebrew', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(default='None', max_length=4000)),
                ('flavour', models.CharField(default='None', max_length=4000)),
                ('strbonus', models.IntegerField(default=0)),
                ('dexbonus', models.IntegerField(default=0)),
                ('intbonus', models.IntegerField(default=0)),
                ('wisbonus', models.IntegerField(default=0)),
                ('chabonus', models.IntegerField(default=0)),
                ('conbonus', models.IntegerField(default=0)),
                ('ageadult', models.IntegerField(default=0)),
                ('agemax', models.IntegerField(default=0)),
                ('alignment', models.CharField(default='None', max_length=4000)),
                ('heightavg', models.FloatField(default=0)),
                ('size', models.CharField(default='None', max_length=4000)),
                ('speed', models.IntegerField(default=0)),
                ('lang1', models.CharField(default='None', max_length=4000)),
                ('lang2', models.CharField(default='None', max_length=4000)),
                ('lang3', models.CharField(default='None', max_length=4000)),
                ('toolprof1', models.CharField(default='None', max_length=4000)),
                ('toolprof2', models.CharField(default='None', max_length=4000)),
                ('toolprof3', models.CharField(default='None', max_length=4000)),
                ('weaponprof1', models.CharField(default='None', max_length=4000)),
                ('weaponprof2', models.CharField(default='None', max_length=4000)),
                ('weaponprof3', models.CharField(default='None', max_length=4000)),
                ('homebrew', models.BooleanField(default=True)),
                ('feature1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature1', to='charactermanager.Feature')),
                ('feature2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature2', to='charactermanager.Feature')),
                ('feature3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature3', to='charactermanager.Feature')),
                ('feature4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature4', to='charactermanager.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(default='None', max_length=4000)),
            ],
        ),
    ]
