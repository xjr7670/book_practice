# Generated by Django 2.1.4 on 2023-04-20 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('birthday', models.DateField(verbose_name='出生日期')),
                ('header', models.ImageField(upload_to='', verbose_name='作者头像')),
            ],
            options={
                'verbose_name': '作者基本情况',
                'verbose_name_plural': '作者基本情况',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='图书名称')),
                ('descript', models.TextField(verbose_name='书籍简介')),
                ('publishdate', models.DateField(verbose_name='出版日期')),
                ('author', models.ManyToManyField(to='book.Author', verbose_name='作者')),
            ],
            options={
                'verbose_name': '图书信息',
                'verbose_name_plural': '图书信息',
            },
        ),
        migrations.CreateModel(
            name='Publishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='出版社名称')),
                ('address', models.CharField(max_length=20, verbose_name='出版社地址')),
            ],
            options={
                'verbose_name': '出版社信息',
                'verbose_name_plural': '出版社书信息',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Publishing', verbose_name='出版社'),
        ),
    ]