# Generated by Django 4.0.6 on 2022-08-24 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TallyApp', '0005_subgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maingroup',
            old_name='nature',
            new_name='under_group',
        ),
    ]