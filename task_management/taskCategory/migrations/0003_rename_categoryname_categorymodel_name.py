# Generated by Django 4.2.7 on 2023-12-07 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskCategory', '0002_remove_categorymodel_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='categoryName',
            new_name='name',
        ),
    ]
