# Generated by Django 3.1.1 on 2021-08-02 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cip', '0012_auto_20210801_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bienpat',
            name='codEti',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='dependencia',
            name='codDep',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
