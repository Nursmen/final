# Generated by Django 4.0.6 on 2022-07-17 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0004_remove_day_program_program_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='program',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='sport.day'),
        ),
    ]
