# Generated by Django 4.2.4 on 2023-09-18 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
    ]
