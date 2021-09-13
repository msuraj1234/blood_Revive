# Generated by Django 3.2.7 on 2021-09-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(default=None, max_length=10)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('others', models.TextField(max_length=100)),
            ],
        ),
    ]
