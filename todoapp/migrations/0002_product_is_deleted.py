# Generated by Django 4.1.1 on 2022-10-05 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_deleted',
            field=models.CharField(default='N', max_length=5),
            preserve_default=False,
        ),
    ]
