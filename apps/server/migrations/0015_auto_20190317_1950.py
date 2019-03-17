# Generated by Django 2.1 on 2019-03-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0014_auto_20190317_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='approach_date',
            field=models.DateField(blank=True, help_text='进场日期', max_length=32, verbose_name='进场日期'),
        ),
        migrations.AlterField(
            model_name='server',
            name='expire_date',
            field=models.DateField(blank=True, help_text='过保日期', max_length=32, verbose_name='过保日期'),
        ),
    ]
