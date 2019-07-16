# Generated by Django 2.1.4 on 2019-04-29 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cust',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Customer'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
            preserve_default=False,
        ),
    ]
