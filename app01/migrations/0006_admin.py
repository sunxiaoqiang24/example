# Generated by Django 4.0.4 on 2022-05-01 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_alter_prettynum_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
    ]
