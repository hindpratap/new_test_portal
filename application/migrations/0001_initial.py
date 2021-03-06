# Generated by Django 2.2.7 on 2019-12-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('option1', models.CharField(blank=True, max_length=500, null=True)),
                ('option2', models.CharField(blank=True, max_length=500, null=True)),
                ('option3', models.CharField(blank=True, max_length=500, null=True)),
                ('option4', models.CharField(blank=True, max_length=500, null=True)),
                ('correct', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tagquestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('quesid', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
