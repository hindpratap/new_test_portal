# Generated by Django 2.2.7 on 2019-12-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20191226_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option5',
            field=models.TextField(blank=True, default='null', null=True),
        ),
    ]
