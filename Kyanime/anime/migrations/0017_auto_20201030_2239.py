# Generated by Django 3.1.2 on 2020-10-31 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0016_auto_20201030_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_anime', models.CharField(max_length=100)),
                ('episodios', models.IntegerField(default=0)),
                ('sinopsis', models.TextField(help_text='Resumen de que trata el Anime')),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
