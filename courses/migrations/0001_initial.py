# Generated by Django 3.1.5 on 2021-04-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=100)),
                ('olevel_subjects', models.TextField()),
                ('jamb_subject', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'ordering': ['-time'],
            },
        ),
    ]