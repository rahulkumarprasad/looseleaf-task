# Generated by Django 3.2.12 on 2022-03-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=500)),
                ('standard', models.CharField(max_length=500)),
                ('iscompulsory', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('standard', models.IntegerField()),
                ('cources', models.ManyToManyField(to='api.Courses')),
            ],
        ),
    ]