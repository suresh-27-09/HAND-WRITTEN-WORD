# Generated by Django 4.2.9 on 2024-02-07 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_mark_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='roll_no',
            field=models.CharField(max_length=30),
        ),
    ]
