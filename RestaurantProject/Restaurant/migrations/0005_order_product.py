# Generated by Django 3.1.1 on 2020-10-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0004_auto_20201012_0305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=300)),
                ('ProductQty', models.CharField(max_length=300)),
                ('ProductPrice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OId', models.AutoField(primary_key=True, serialize=False)),
                ('TPrice', models.CharField(default='', max_length=400)),
                ('Allproduct', models.ManyToManyField(to='Restaurant.Product')),
            ],
        ),
    ]
