# Generated by Django 4.0.2 on 2022-05-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moshavere', '0014_consulation_daneshjoo_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulation',
            name='erja_ravanpezeshk',
            field=models.BooleanField(default=False),
        ),
    ]