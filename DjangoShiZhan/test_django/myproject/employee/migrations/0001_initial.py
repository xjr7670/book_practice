# Generated by Django 2.1.4 on 2023-03-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=32, verbose_name='团体名称')),
                ('group_script', models.CharField(max_length=60, verbose_name='备注')),
            ],
        ),
    ]
