# Generated by Django 2.1.4 on 2019-01-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190104_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_desc',
            field=models.TextField(max_length=600),
        ),
    ]