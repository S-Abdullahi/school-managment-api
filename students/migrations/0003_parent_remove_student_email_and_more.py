# Generated by Django 4.1.1 on 2022-09-24 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_parent_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('occupation', models.CharField(blank=True, max_length=255)),
                ('parent_phone', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parent_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parent_phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=10),
        ),
    ]