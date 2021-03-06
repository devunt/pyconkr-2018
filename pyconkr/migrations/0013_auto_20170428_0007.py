# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pyconkr', '0012_auto_20160727_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='banner'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='program',
            name='difficulty',
            field=models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('E', 'Experienced')], default='B', max_length=1),
        ),
        migrations.AlterField(
            model_name='program',
            name='duration',
            field=models.CharField(choices=[('S', '25 mins'), ('L', '40 mins')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='program',
            name='language',
            field=models.CharField(choices=[('E', 'English'), ('K', 'Korean')], default='E', max_length=1),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='difficulty',
            field=models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('E', 'Experienced')], max_length=1),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='duration',
            field=models.CharField(choices=[('S', '25 mins'), ('L', '40 mins')], max_length=1),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='language',
            field=models.CharField(choices=[('E', 'English'), ('K', 'Korean')], default='E', max_length=1),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='speaker'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sponsor'),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='capacity',
            field=models.CharField(choices=[('S', '10 people'), ('M', '45 people'), ('L', '100 people')], max_length=1),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='difficulty',
            field=models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('E', 'Experienced')], max_length=1),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='duration',
            field=models.CharField(choices=[('S', '1 hour'), ('M', '2 hours'), ('L', '4 hours')], max_length=1),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='language',
            field=models.CharField(choices=[('E', 'English'), ('K', 'Korean')], default='E', max_length=1),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='type',
            field=models.CharField(choices=[('T', 'Tutorial'), ('S', 'Sprint')], default='T', max_length=1),
        ),
    ]
