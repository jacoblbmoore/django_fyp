# Generated by Django 4.1.7 on 2023-03-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablecombination',
            old_name='combined_tables',
            new_name='tables',
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.TextField(),
        ),
    ]