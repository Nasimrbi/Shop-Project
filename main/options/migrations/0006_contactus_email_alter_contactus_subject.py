# Generated by Django 5.0.3 on 2024-08-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0005_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F'), ('g', 'G'), ('h', 'H')], max_length=255),
        ),
    ]
