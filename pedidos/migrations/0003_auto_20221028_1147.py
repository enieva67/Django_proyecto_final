# Generated by Django 3.1 on 2022-10-28 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20221020_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financiacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuotas', models.IntegerField(default=1)),
                ('importe_cuota', models.FloatField()),
                ('forma_de_pago', models.CharField(default='contado efectivo', max_length=30)),
            ],
            options={
                'verbose_name': 'Financiacion',
                'verbose_name_plural': 'Financiacion',
                'db_table': 'financiacion',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='lineapedido',
            name='financiacion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pedidos.financiacion'),
        ),
    ]
