# Generated by Django 2.2.5 on 2019-10-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manna', '0010_auto_20191022_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ongoing',
            field=models.BooleanField(default=True),
        ),
    ]
