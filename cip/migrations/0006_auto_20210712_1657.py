# Generated by Django 3.1.1 on 2021-07-12 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cip', '0005_auto_20210712_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codAmb', models.CharField(max_length=11)),
                ('descAmb', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='bienpat',
            name='codAmb',
        ),
        migrations.RemoveField(
            model_name='bienpat',
            name='codDep',
        ),
        migrations.AddField(
            model_name='bienpat',
            name='ambiente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cip.ambiente'),
            preserve_default=False,
        ),
    ]
