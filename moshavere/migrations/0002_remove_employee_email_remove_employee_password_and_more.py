# Generated by Django 4.0.2 on 2022-02-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moshavere', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='password',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='test',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='username',
        ),
        migrations.AddField(
            model_name='employee',
            name='job',
            field=models.CharField(choices=[('moshaver', 'MOSHAVER'), ('employee', 'EMPLOYEE')], default='moshaver', max_length=8),
        ),
        migrations.AddField(
            model_name='employee',
            name='meli_code',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
