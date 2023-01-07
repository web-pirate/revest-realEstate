# Generated by Django 4.1.4 on 2023-01-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_property_property_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForgotPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('is_checked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
