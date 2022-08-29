# Generated by Django 4.1 on 2022-08-29 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TallyApp', '0016_ledger_ledger_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger',
            name='l_sundry',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='l_tax',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='ledger_bank',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='ledger_mail',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='ledger_round',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='ledger_sat',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='ledger_tax',
        ),
        migrations.AddField(
            model_name='l_tax_register',
            name='ledger_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AddField(
            model_name='ledger_banking_details',
            name='ledger_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AddField(
            model_name='ledger_mailing_address',
            name='ledger_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AddField(
            model_name='ledger_rounding',
            name='ledger_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AddField(
            model_name='ledger_satutory',
            name='ledger_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AddField(
            model_name='ledger_sundry',
            name='ledger_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
        migrations.AddField(
            model_name='ledger_tax',
            name='ledger_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TallyApp.ledger'),
        ),
    ]
