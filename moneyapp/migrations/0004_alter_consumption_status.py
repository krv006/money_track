# Generated by Django 5.0.1 on 2024-02-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneyapp', '0003_alter_consumption_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='status',
            field=models.IntegerField(choices=[(1, 'not_gived'), (2, 'paid'), (3, 'not_paid'), (4, 'pending')], default=1),
        ),
    ]