# Generated by Django 4.0.6 on 2022-08-26 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TallyApp', '0010_ledger_tax_register_ledger_tax_ledger_sundry_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger_mailing_address',
            name='ledger_bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger_banking_details'),
        ),
    ]
