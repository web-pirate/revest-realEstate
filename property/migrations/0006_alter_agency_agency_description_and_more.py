# Generated by Django 4.1.4 on 2022-12-22 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_agency_agency_created_at_agent_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='agency_description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='agency',
            name='agency_facebook',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='agency',
            name='agency_instagram',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agency',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
