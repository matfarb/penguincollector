# Generated by Django 3.2.8 on 2021-10-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swimming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('E', 'Evening')], default='M', max_length=1)),
            ],
        ),
    ]
