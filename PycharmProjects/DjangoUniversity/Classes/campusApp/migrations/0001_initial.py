# Generated by Django 4.1.7 on 2023-03-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campus_Name', models.CharField(blank=True, default='', max_length=55)),
                ('State', models.CharField(blank=True, default='', max_length=2)),
                ('Campus_ID', models.IntegerField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'University Campus',
            },
        ),
    ]
