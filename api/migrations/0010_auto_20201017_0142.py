# Generated by Django 3.0.10 on 2020-10-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201017_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_type',
            new_name='types',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='nKuJKnKOn0', max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='c_user',
            field=models.CharField(default='pCavuq3ivz7zpFpk', max_length=20, unique=True),
        ),
    ]
