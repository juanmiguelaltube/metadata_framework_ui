# Generated by Django 3.2.9 on 2021-11-11 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='metadata',
            unique_together={('field', 'factory')},
        ),
    ]