# Generated by Django 4.0.6 on 2022-08-25 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TallyApp', '0007_alter_maingroup_affect_gp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_name', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_alias', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_opening_bal', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_type', models.CharField(blank=True, default='Null', max_length=225)),
                ('subgroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.subgroup')),
            ],
        ),
    ]
