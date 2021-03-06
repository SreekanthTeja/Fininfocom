# Generated by Django 3.2.3 on 2021-05-28 16:54

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(verbose_name='Phone')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=10, verbose_name='Gender')),
                ('address', models.TextField(verbose_name='Adress')),
                ('avatar', models.FileField(upload_to='', verbose_name='Avater')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=250, verbose_name='Course')),
                ('college', models.CharField(max_length=250, verbose_name='School/College')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('percentage', models.FloatField(verbose_name='Percentage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
