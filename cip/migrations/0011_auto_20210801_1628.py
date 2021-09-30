# Generated by Django 3.1.1 on 2021-08-01 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cip', '0010_auto_20210801_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bienpat',
            name='ambiente',
        ),
        migrations.CreateModel(
            name='bienAmbiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cip.ambiente')),
                ('bienpat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cip.bienpat')),
            ],
        ),
    ]
