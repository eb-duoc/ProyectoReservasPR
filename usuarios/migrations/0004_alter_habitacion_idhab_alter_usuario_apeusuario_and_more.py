# Generated by Django 4.2.5 on 2023-10-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_idusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='idHab',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id de habitacion'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apeUsuario',
            field=models.CharField(default='', max_length=20, verbose_name='apellido de usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.CharField(default='', max_length=20, verbose_name='correo de usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pais',
            field=models.CharField(default='', max_length=20, verbose_name='pais'),
        ),
    ]
