# Generated by Django 5.0.7 on 2024-07-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meca', '0003_rename_teclado_user_keyboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='keyboard',
            field=models.CharField(choices=[('Membrana', 'Membrana'), ('Mecanico', 'Mecanico')], default='Mecanico', max_length=10),
        ),
    ]
