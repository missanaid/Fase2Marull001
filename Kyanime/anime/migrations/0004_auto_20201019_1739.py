# Generated by Django 3.1.2 on 2020-10-19 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0003_auto_20201019_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]