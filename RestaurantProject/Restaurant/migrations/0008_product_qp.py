# Generated by Django 3.1.1 on 2020-10-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0007_ordert_odate'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='QP',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]