# Generated by Django 4.2.4 on 2023-08-28 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_alter_hydjobs_address_alter_hydjobs_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bangjobs',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bangjobs',
            name='company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bangjobs',
            name='eligibility',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bangjobs',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
