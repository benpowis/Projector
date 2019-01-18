# Generated by Django 2.1.4 on 2019-01-04 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190104_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='due date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_desc',
            field=models.TextField(max_length=600),
        ),
    ]