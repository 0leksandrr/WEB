# Generated by Django 5.0 on 2024-01-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='teachers/')),
            ],
        ),
    ]
