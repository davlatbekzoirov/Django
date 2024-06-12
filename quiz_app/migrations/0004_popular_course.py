# Generated by Django 5.0 on 2023-12-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_remove_add_jobs_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('students', models.CharField(max_length=350)),
                ('time', models.CharField(max_length=350)),
                ('title', models.CharField(max_length=350)),
                ('price', models.CharField(max_length=350)),
            ],
            options={
                'verbose_name_plural': 'Popular Course',
            },
        ),
    ]