# Generated by Django 5.0.3 on 2024-03-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='employee',
        ),
        migrations.AddField(
            model_name='booking',
            name='contact_email',
            field=models.EmailField(default='example@example.com', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='full_name',
            field=models.CharField(default='John Doe', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='location',
            field=models.CharField(default='Default Location', max_length=100),
        ),
    ]
