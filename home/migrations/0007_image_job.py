# Generated by Django 4.2.7 on 2023-11-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]