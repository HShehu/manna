# Generated by Django 2.2.5 on 2019-10-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manna', '0008_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='phone_no',
            name='mail',
        ),
    ]
