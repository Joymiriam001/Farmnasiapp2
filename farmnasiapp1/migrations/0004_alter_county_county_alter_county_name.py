# Generated by Django 5.1.4 on 2024-12-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmnasiapp1', '0003_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='county',
            field=models.CharField(choices=[('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu')], max_length=100),
        ),
        migrations.AlterField(
            model_name='county',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
