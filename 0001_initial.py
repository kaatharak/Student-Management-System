# Generated by Django 4.2.8 on 2023-12-27 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('City', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
            ],
        ),
    ]
