# Generated by Django 2.2.24 on 2021-11-23 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_list_item_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default='', to='lists.List'),
        ),
    ]