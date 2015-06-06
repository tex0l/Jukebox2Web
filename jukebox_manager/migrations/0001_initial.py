# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('selection', models.CharField(help_text=b"if not blank, then it's the current musicset for letter id here", max_length=1)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SlotPair',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot1_nb', models.IntegerField(help_text=b'is the number of the final index. Ex: id 1 for index A1 ')),
                ('slot2_nb', models.IntegerField(help_text=b'is the number of the final index. Ex: id 2 for index A2 ')),
                ('artwork', models.ImageField(upload_to=b'Artwork')),
                ('artwork_pk', models.IntegerField(default=0)),
                ('music1', models.ForeignKey(related_name='+', blank=True, to='library_manager.Music', null=True)),
                ('music2', models.ForeignKey(related_name='+', blank=True, to='library_manager.Music', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='musicset',
            name='s0',
            field=models.ForeignKey(related_name='+', to='jukebox_manager.SlotPair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='musicset',
            name='s1',
            field=models.ForeignKey(related_name='+', to='jukebox_manager.SlotPair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='musicset',
            name='s2',
            field=models.ForeignKey(related_name='+', to='jukebox_manager.SlotPair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='musicset',
            name='s3',
            field=models.ForeignKey(related_name='+', to='jukebox_manager.SlotPair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='musicset',
            name='s4',
            field=models.ForeignKey(related_name='+', to='jukebox_manager.SlotPair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='musicset',
            name='s5',
            field=models.ForeignKey(related_name='+', to='jukebox_manager.SlotPair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='musicset',
            name='s6',
            field=models.ForeignKey(related_name='+', to='jukebox_manager.SlotPair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='musicset',
            name='s7',
            field=models.ForeignKey(related_name='+', to='jukebox_manager.SlotPair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='musicset',
            name='s8',
            field=models.ForeignKey(related_name='+', to='jukebox_manager.SlotPair'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='musicset',
            name='s9',
            field=models.ForeignKey(related_name='+', to='jukebox_manager.SlotPair'),
            preserve_default=True,
        ),
    ]
