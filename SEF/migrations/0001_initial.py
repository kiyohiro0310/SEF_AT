# Generated by Django 4.2.5 on 2023-10-25 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('image_path', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('suburb', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('fee', models.PositiveIntegerField()),
                ('date_added', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=300)),
                ('last_login', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval', models.CharField(max_length=20)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEF.pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEF.user')),
            ],
        ),
    ]
