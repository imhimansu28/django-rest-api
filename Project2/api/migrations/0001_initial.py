# Generated by Django 4.0.3 on 2022-03-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=100)),
                ('stu_class', models.IntegerField()),
                ('stu_phone', models.CharField(max_length=20)),
                ('stu_roll', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
