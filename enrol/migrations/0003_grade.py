# Generated by Django 3.2 on 2021-04-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrol', '0002_auto_20210422_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]