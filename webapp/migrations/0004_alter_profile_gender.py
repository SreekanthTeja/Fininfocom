# Generated by Django 3.2.3 on 2021-05-30 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_education_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=10, verbose_name='Gender'),
        ),
    ]
