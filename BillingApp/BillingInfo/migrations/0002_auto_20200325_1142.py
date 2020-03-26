# Generated by Django 3.0.4 on 2020-03-25 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BillingInfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billinfo',
            old_name='cost',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='billinfo',
            old_name='bill_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='billinfo',
            old_name='bill_release_date',
            new_name='event_time',
        ),
        migrations.AlterModelTable(
            name='billinfo',
            table=None,
        ),
    ]
