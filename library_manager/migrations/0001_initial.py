# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'unknown', max_length=b'100')),
                ('year', models.CharField(max_length=b'100', null=True, blank=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('number_of_tracks', models.IntegerField(null=True, blank=True)),
                ('number_of_discs', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'unknown', max_length=b'100')),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'Artwork', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArtistArtwork',
            fields=[
                ('artwork_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='library_manager.Artwork')),
                ('artist', models.ForeignKey(related_name='+', blank=True, to='library_manager.Artist', null=True)),
            ],
            options={
            },
            bases=('library_manager.artwork',),
        ),
        migrations.CreateModel(
            name='AlbumArtwork',
            fields=[
                ('artwork_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='library_manager.Artwork')),
                ('album', models.ForeignKey(related_name='+', blank=True, to='library_manager.Album', null=True)),
            ],
            options={
            },
            bases=('library_manager.artwork',),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'title')),
                ('year', models.CharField(max_length=b'100', null=True, blank=True)),
                ('file_field', models.FileField(upload_to=b'Library')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('track_number', models.IntegerField(null=True, blank=True)),
                ('disc_number', models.IntegerField(null=True, blank=True)),
                ('album', models.ForeignKey(blank=True, to='library_manager.Album', null=True)),
                ('artist', models.ForeignKey(blank=True, to='library_manager.Artist', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SlotArtwork',
            fields=[
                ('artwork_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='library_manager.Artwork')),
            ],
            options={
            },
            bases=('library_manager.artwork',),
        ),
        migrations.AddField(
            model_name='artist',
            name='artwork',
            field=models.ForeignKey(related_name='+', blank=True, to='library_manager.ArtistArtwork', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='album_artist',
            field=models.ForeignKey(blank=True, to='library_manager.Artist', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='artwork',
            field=models.ForeignKey(related_name='+', blank=True, to='library_manager.AlbumArtwork', null=True),
            preserve_default=True,
        ),
    ]
