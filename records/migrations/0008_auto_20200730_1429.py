# Generated by Django 3.0.6 on 2020-07-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_pledge_settled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='contributed',
            field=models.IntegerField(default=0),
        ),
    ]
