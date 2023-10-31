# Generated by Django 4.2.6 on 2023-10-31 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textbook_app', '0003_book_wantedbook_ownedbook_borrowedbook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowedbook',
            old_name='user_id',
            new_name='borrower',
        ),
        migrations.AddField(
            model_name='borrowedbook',
            name='ownedbook',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='textbook_app.ownedbook'),
        ),
    ]