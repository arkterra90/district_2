# Generated by Django 4.2.2 on 2023-12-23 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_voter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='birth_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='cde_name_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='date_of_voter_reg',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='ind_mail_foreign',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='voter',
            name='ind_mail_military',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='voter',
            name='ind_res_military',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='voter',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='political_party',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='precinct_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='reg_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='registration_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='street_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='zip',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]