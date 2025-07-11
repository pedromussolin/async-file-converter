# Generated by Django 5.2.4 on 2025-07-09 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('extension', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_file', models.FileField(upload_to='uploads/')),
                ('output_file', models.FileField(blank=True, null=True, upload_to='converted/')),
                ('status', models.CharField(choices=[('pending', 'Pendente'), ('processing', 'Processando'), ('done', 'Concluído'), ('failed', 'Falhou')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('log', models.TextField(blank=True)),
                ('input_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_type', to='app_converter.filetype')),
                ('output_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='output_type', to='app_converter.filetype')),
            ],
        ),
    ]
