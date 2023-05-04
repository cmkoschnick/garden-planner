# Generated by Django 4.1.4 on 2023-05-04 03:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gardenbed', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bed',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='bed',
            name='id',
            field=models.SmallIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='bed',
            unique_together={('user', 'location', 'id')},
        ),
    ]