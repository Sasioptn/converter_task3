# Generated by Django 2.2.2 on 2019-06-09 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
