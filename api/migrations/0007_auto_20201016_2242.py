# Generated by Django 3.0.10 on 2020-10-16 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201016_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='mRXW1cKZuc', max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='types',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='styles', to='api.style'),
        ),
        migrations.AlterField(
            model_name='user',
            name='c_user',
            field=models.CharField(default='JOEcUq25wH0sWVR5', max_length=20, unique=True),
        ),
    ]
