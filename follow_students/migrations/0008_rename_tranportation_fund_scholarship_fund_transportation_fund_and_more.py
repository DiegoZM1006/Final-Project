# Generated by Django 4.2.5 on 2023-10-06 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_students', '0007_student_aux_academic_student_aux_transporte'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scholarship_fund',
            old_name='tranportation_fund',
            new_name='transportation_fund',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='aux_transporte',
            new_name='aux_transportation',
        ),
    ]
