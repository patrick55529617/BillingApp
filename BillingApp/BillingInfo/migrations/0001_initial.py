# Generated by Django 3.0.3 on 2020-03-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_content', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('bill_release_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'BillInfo',
            },
        ),
    ]