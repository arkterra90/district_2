# Generated by Django 4.2.2 on 2024-02-10 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
    ]