# Generated by Django 2.2.4 on 2021-01-24 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='content',
            field=models.TextField(null=True),
        ),
    ]