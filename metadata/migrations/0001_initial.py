# Generated by Django 3.2.9 on 2021-11-11 12:40

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
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'CBS',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Factories',
                'ordering': ['id'],
            },
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
            options={
                'verbose_name_plural': 'Schema Fields',
                'ordering': ['field'],
            },
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(blank=True, max_length=255)),
                ('format_in', models.CharField(blank=True, max_length=255)),
                ('format_out', models.CharField(blank=True, max_length=255)),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.factory')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.schemafield')),
            ],
            options={
                'verbose_name_plural': 'Metadatas',
                'ordering': ['field'],
            },
        ),
    ]
