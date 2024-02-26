# Generated by Django 3.2 on 2024-02-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20240204_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='animales',
            name='tratamiento',
            field=models.CharField(choices=[('CM', 'consulta medica'), ('UR', 'Urgencia'), ('OB', 'Observacion regular'), ('TQ', 'Tratamiento quirurgico'), ('SO', 'Sin observacines')], default='SO', max_length=2),
        ),
    ]