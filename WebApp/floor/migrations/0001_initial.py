# Generated by Django 2.2.4 on 2019-10-07 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
                ('roomCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomID', models.CharField(max_length=5)),
                ('occupied', models.IntegerField()),
                ('lastExited', models.DateField()),
                ('lastEntered', models.DateField()),
                ('roomType', models.CharField(default='S', max_length=6)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floor.Floor')),
            ],
        ),
    ]
