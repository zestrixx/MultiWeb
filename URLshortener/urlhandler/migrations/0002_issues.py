# Generated by Django 3.1.5 on 2021-06-17 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlhandler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('issueId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('query', models.CharField(max_length=100)),
            ],
        ),
    ]
