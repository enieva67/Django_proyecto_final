# Generated by Django 4.1 on 2022-11-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afterselling', '0002_encuesta_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
