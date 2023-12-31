# Generated by Django 4.2.2 on 2023-12-10 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formName', models.CharField(max_length=255)),
                ('formEmail', models.CharField(max_length=255)),
                ('formPhone', models.CharField(max_length=20)),
                ('formMessage', models.TextField()),
                ('formVolunteer', models.BooleanField(default=False)),
                ('formYardSign', models.BooleanField(default=False)),
                ('formDoorHangers', models.BooleanField(default=False)),
                ('formLargeSign', models.BooleanField(default=False)),
                ('formMeetAndGreet', models.BooleanField(default=False)),
            ],
        ),
    ]
