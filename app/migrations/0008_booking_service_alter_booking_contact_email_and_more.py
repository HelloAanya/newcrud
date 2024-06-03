# Generated by Django 5.0.3 on 2024-03-30 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_booking_employee_booking_contact_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='service',
            field=models.CharField(default='Default Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='contact_email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]