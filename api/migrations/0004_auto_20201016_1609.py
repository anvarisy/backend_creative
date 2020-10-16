# Generated by Django 3.0.10 on 2020-10-16 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201016_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='style',
            name='style_fbody',
        ),
        migrations.RemoveField(
            model_name='style',
            name='style_head',
        ),
        migrations.RemoveField(
            model_name='style',
            name='style_hnb',
        ),
        migrations.RemoveField(
            model_name='style',
            name='style_hnc',
        ),
        migrations.RemoveField(
            model_name='style',
            name='style_icon',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='IK9uD2RF2r', max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_result',
            field=models.FileField(default='#', upload_to='result'),
        ),
        migrations.AlterField(
            model_name='user',
            name='c_user',
            field=models.CharField(default='4aELfwFX3gEJ5qPW', max_length=20, unique=True),
        ),
        migrations.CreateModel(
            name='types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=60)),
                ('type_icon', models.ImageField(upload_to='types')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.style')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.types'),
            preserve_default=False,
        ),
    ]
