# Generated by Django 3.0.10 on 2020-10-16 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_finish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='PIk1bnRh3J', max_length=12, primary_key=True, serialize=False),
        ),
    ]
