# Generated by Django 5.1.6 on 2025-02-25 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('size', models.IntegerField(default=2)),
                ('text1', models.CharField(max_length=255)),
            ],
        ),
    ]
