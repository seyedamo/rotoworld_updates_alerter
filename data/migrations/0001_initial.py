# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('rotoworld_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.TextField()),
                ('impact', models.TextField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=10)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.League')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='sport',
            unique_together=set([('name', 'abbreviation')]),
        ),
        migrations.AddField(
            model_name='position',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Sport'),
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Position'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Team'),
        ),
        migrations.AddField(
            model_name='league',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Sport'),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([('league', 'name', 'abbreviation')]),
        ),
        migrations.AlterUniqueTogether(
            name='position',
            unique_together=set([('sport', 'name', 'abbreviation')]),
        ),
        migrations.AlterUniqueTogether(
            name='playernews',
            unique_together=set([('player', 'report', 'impact')]),
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('team', 'position', 'first_name', 'last_name', 'rotoworld_url')]),
        ),
        migrations.AlterUniqueTogether(
            name='league',
            unique_together=set([('sport', 'name', 'abbreviation')]),
        ),
    ]
