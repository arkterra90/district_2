# Generated by Django 4.2.2 on 2023-12-23 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_voter_address_alter_voter_birth_year_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Voter',
        ),
    ]
