# Generated by Django 3.0.5 on 2020-05-22 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pno', models.IntegerField()),
                ('pdetails', models.CharField(max_length=30)),
                ('paddr', models.CharField(max_length=30)),
            ],
        ),
    ]