# Generated by Django 4.2.1 on 2023-05-25 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]