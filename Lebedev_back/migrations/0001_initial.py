# Generated by Django 5.0.4 on 2024-04-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('nativeId', models.CharField(max_length=100)),
                ('nativeName', models.CharField(max_length=100)),
            ],
        ),
    ]
