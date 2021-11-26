# Generated by Django 3.2.9 on 2021-11-26 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=100)),
                ('job_type', models.CharField(blank=True,
                                              choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')],
                                              default='2', max_length=15, null=True)),
                ('company_name', models.CharField(max_length=255)),
                ('company_description', models.CharField(max_length=255)),
                ('post_until', models.DateField()),
                ('is_active', models.BooleanField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='job_author',
                                                to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
