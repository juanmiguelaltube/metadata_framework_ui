# Generated by Django 3.2.9 on 2021-11-09 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CBS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'CBS',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SchemaField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=255)),
                ('whitelist', models.BooleanField(default=False)),
                ('cbs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.cbs')),
                ('data_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.datasource')),
            ],
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('params', models.CharField(max_length=255)),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.factory')),
                ('schema_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.schemafield')),
            ],
            options={
                'verbose_name_plural': 'Metadata',
                'ordering': ['schema_field'],
            },
        ),
    ]
