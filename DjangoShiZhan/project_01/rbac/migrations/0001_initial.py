# Generated by Django 2.1.4 on 2023-04-25 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='Top Level Menu')),
            ],
            options={
                'verbose_name_plural': 'Top Level Menu',
            },
        ),
        migrations.CreateModel(
            name='PermGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Group name')),
                ('menu', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Menu', verbose_name='Belonging Menu')),
            ],
            options={
                'verbose_name_plural': 'Authority Group',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='Authority Name')),
                ('url', models.CharField(max_length=128, unique=True, verbose_name='URL')),
                ('perm_code', models.CharField(max_length=32, verbose_name='Authority Code')),
                ('perm_group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.PermGroup', verbose_name='Belonging Authority Group')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Permission', verbose_name='Belonging Second Menu')),
            ],
            options={
                'verbose_name_plural': 'Authority Table',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='Role Name')),
                ('permissions', models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='Permissions')),
            ],
            options={
                'verbose_name_plural': 'Role Table',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('nickname', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('roles', models.ManyToManyField(to='rbac.Role')),
            ],
            options={
                'verbose_name_plural': 'User Table',
            },
        ),
    ]