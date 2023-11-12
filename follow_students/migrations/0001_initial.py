# Generated by Django 4.2.5 on 2023-11-12 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='23', max_length=20, unique=True)),
                ('transporte', models.IntegerField()),
                ('alimentacion', models.IntegerField()),
                ('academico', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('mail', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NonAcademicActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_permiso', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('assigned_students', models.PositiveIntegerField(default=0)),
                ('porcentaje_academico', models.IntegerField(default=70)),
                ('auxilio_transporte', models.IntegerField(default=1000000)),
                ('amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.amount')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.donor')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('icfes', models.IntegerField()),
                ('cedula', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('mail', models.EmailField(max_length=254)),
                ('aux_transportation', models.CharField(default=0, max_length=100)),
                ('aux_academic', models.CharField(default=0, max_length=100)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.major')),
                ('scholarship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='follow_students.scholarship')),
            ],
        ),
        migrations.CreateModel(
            name='RolPermiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.permiso')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.rol')),
            ],
        ),
        migrations.CreateModel(
            name='RegisNonAcademicActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistance_days', models.CharField(max_length=100)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.nonacademicactivity')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.student')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.student')),
            ],
        ),
        migrations.CreateModel(
            name='Gasto_beca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_dinero', models.FloatField()),
                ('tiempo_acumulado', models.IntegerField()),
                ('tiempo_seleccionado', models.CharField(choices=[('1', 'Dias'), ('2', 'Mes'), ('3', 'Año')], default='1', max_length=2)),
                ('tipo', models.CharField(max_length=20)),
                ('scholarship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='follow_students.scholarship')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='follow_students.student')),
            ],
        ),
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('reason', models.TextField()),
                ('outcome', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_students.student')),
            ],
        ),
    ]
