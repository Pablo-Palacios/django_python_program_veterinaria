# Generated by Django 3.2 on 2024-02-04 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroConsultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('dueño', models.CharField(max_length=20)),
                ('dni_dueño', models.IntegerField()),
                ('animal', models.CharField(max_length=20)),
                ('animal_categoria', models.CharField(max_length=20)),
                ('tratamiento', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='animales',
            name='tratamiento',
        ),
    ]
