# Generated by Django 3.0.10 on 2020-10-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201016_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='style_icon',
            field=models.ImageField(blank=True, upload_to='style'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='ELU1fzAnmJ', max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='c_user',
            field=models.CharField(default='ZTU1wlYJoE2oSjrx', max_length=20, unique=True),
        ),
    ]
