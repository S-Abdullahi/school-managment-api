# Generated by Django 4.0.6 on 2022-10-14 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_school_remove_student_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarystudent',
            name='level',
            field=models.CharField(blank=True, choices=[('CRECHE', 'CRECHE'), ('NURSERY', 'NURSERY'), ('PRIMARY', 'PRIMARY')], max_length=255, null=True),
        ),
    ]
