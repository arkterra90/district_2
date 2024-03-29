# Generated by Django 4.2.2 on 2024-02-10 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_delete_voter'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=15)),
                ('dateMade', models.DateField()),
                ('text', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
