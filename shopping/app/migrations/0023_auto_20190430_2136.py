# Generated by Django 2.1.4 on 2019-04-30 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cust',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer'),
        ),
    ]