# Generated by Django 3.2 on 2022-09-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_parent_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='parent_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
