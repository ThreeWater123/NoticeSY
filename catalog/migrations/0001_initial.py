# Generated by Django 4.1.7 on 2023-03-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('notice', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
