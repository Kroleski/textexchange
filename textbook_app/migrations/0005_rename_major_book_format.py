# Generated by Django 4.2.6 on 2023-10-31 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textbook_app', '0004_rename_user_id_borrowedbook_borrower_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='major',
            new_name='format',
        ),
    ]