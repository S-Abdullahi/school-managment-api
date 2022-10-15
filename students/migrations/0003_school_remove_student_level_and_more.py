# Generated by Django 4.0.6 on 2022-10-13 12:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_school_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('school_type', models.CharField(blank=True, choices=[('BASIC PRIMARY', 'BASIC PRIMARY'), ('SECONDARY', 'SECONDARY')], max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='level',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school_type',
        ),
        migrations.CreateModel(
            name='SecondaryStudent',
            fields=[
                ('student_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.student')),
                ('level', models.CharField(blank=True, choices=[('JUNIOR SECONDARY', 'JUNIOR SECONDARY'), ('SENIOR SECONDARY', 'SENIOR SECONDARY')], max_length=255, null=True)),
                ('school_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary_school', to='students.student')),
            ],
            options={
                'abstract': False,
            },
            bases=('students.student',),
        ),
        migrations.CreateModel(
            name='PrimaryStudent',
            fields=[
                ('student_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.student')),
                ('level', models.CharField(blank=True, choices=[('CRECHE', 'CRECHE'), ('NURSERY', 'NURSERY'), ('PRIMARY', 'PRIMARY'), ('JUNIOR SECONDARY', 'JUNIOR SECONDARY'), ('SENIOR SECONDARY', 'SENIOR SECONDARY')], max_length=255, null=True)),
                ('school_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_school', to='students.school')),
            ],
            options={
                'abstract': False,
            },
            bases=('students.student',),
        ),
    ]