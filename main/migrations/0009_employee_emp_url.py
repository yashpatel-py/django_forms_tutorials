# Generated by Django 4.2.1 on 2023-07-14 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_employee_emp_files_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
