# Generated by Django 3.0.10 on 2020-10-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20201028_0626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='c_user',
        ),
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='num_character',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='V2FfEYDWca', max_length=12, primary_key=True, serialize=False),
        ),
    ]
