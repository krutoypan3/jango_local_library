# Generated by Django 3.0.5 on 2020-04-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('body', models.ImageField(upload_to='')),
                ('price', models.CharField(max_length=30)),
            ],
        ),
    ]
