# Generated by Django 4.2.2 on 2023-07-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField()),
                ('total_projects', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]