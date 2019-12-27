# Generated by Django 2.2.7 on 2019-12-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authorizedadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CreateCandidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('fullname', models.CharField(blank=True, max_length=300, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('team', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('invitestatus', models.CharField(blank=True, default='Pending', max_length=200, null=True)),
                ('teststatus', models.CharField(blank=True, default='Pending', max_length=200, null=True)),
                ('selectionstatus', models.CharField(blank=True, default='Pending', max_length=200, null=True)),
                ('dob', models.DateField(blank=True, default=None, null=True)),
                ('resume', models.FileField(blank=True, upload_to='')),
                ('created_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('activestatus', models.CharField(blank=True, default='active', max_length=200, null=True)),
            ],
        ),
    ]
