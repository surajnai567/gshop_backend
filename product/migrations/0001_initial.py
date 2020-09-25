# Generated by Django 3.1.1 on 2020-09-22 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('attribute', models.CharField(max_length=20)),
                ('currency', models.CharField(default='Rs.', max_length=5)),
                ('discount', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('homepage', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.categorymodel')),
            ],
        ),
    ]
