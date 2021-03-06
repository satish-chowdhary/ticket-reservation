# Generated by Django 2.1.1 on 2019-02-03 13:31

import bookingapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0002_auto_20190203_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confmd_tkts', models.IntegerField(editable=False, max_length=24, verbose_name=bookingapp.models.Coaches)),
                ('rac_tickets', models.IntegerField(max_length=3, verbose_name=bookingapp.models.Coaches)),
                ('waiting_list', models.PositiveIntegerField(max_length=5, verbose_name=bookingapp.models.Coaches)),
            ],
        ),
        migrations.AlterField(
            model_name='coaches',
            name='S1',
            field=models.ForeignKey(max_length=8, on_delete=django.db.models.deletion.CASCADE, related_name='S1', to='bookingapp.Portions'),
        ),
        migrations.AlterField(
            model_name='coaches',
            name='S2',
            field=models.ForeignKey(max_length=8, on_delete=django.db.models.deletion.CASCADE, related_name='S2', to='bookingapp.Portions'),
        ),
        migrations.AlterField(
            model_name='coaches',
            name='S3',
            field=models.ForeignKey(max_length=8, on_delete=django.db.models.deletion.CASCADE, related_name='S3', to='bookingapp.Portions'),
        ),
        migrations.AlterField(
            model_name='coaches',
            name='S4',
            field=models.ForeignKey(max_length=8, on_delete=django.db.models.deletion.CASCADE, related_name='S4', to='bookingapp.Portions'),
        ),
    ]
