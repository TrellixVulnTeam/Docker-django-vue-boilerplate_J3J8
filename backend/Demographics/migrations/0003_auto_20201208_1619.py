# Generated by Django 3.1.3 on 2020-12-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demographics', '0002_auto_20201208_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographic_answers',
            name='answer',
            field=models.TextField(),
        ),
    ]
