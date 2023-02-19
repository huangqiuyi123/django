# Generated by Django 3.2 on 2023-02-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment', models.CharField(max_length=50, verbose_name='环境')),
                ('link', models.CharField(max_length=2048, verbose_name='链接')),
                ('account', models.CharField(max_length=500, verbose_name='账号')),
                ('password', models.CharField(max_length=500, verbose_name='密码')),
            ],
        ),
    ]