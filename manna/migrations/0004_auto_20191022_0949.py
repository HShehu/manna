# Generated by Django 2.2.5 on 2019-10-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manna', '0003_auto_20191022_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
