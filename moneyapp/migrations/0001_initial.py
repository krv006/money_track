# Generated by Django 5.0 on 2024-01-24 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plastic_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Plastic_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plastic_nmae', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moneyapp.card')),
            ],
        ),
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('time', models.TimeField(null=True)),
                ('status', models.TextField()),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moneyapp.sub_category')),
            ],
        ),
    ]
