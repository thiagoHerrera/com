# Generated by Django 4.1.7 on 2024-09-26 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descricion', models.CharField(max_length=50)),
                ('precio', models.IntegerField(max_length=50)),

            ],
        ),
    ]
