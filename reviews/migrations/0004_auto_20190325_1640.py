# Generated by Django 2.1.7 on 2019-03-25 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20190325_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='product',
        ),
        migrations.AddField(
            model_name='feedback',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.feedback'),
        ),
    ]