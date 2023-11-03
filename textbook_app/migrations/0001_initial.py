# Generated by Django 4.2.6 on 2023-11-03 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('format', models.CharField(choices=[('Hardcover', 'Hardcover'), ('Paperback', 'Paperback'), ('PDF', 'PDF file'), ('Digital', 'Digital file containing the book'), ('Link', 'Link to the book or a free download site')], max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='WantedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='textbook_app.book')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='textbook_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='OwnedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=False)),
                ('condition', models.CharField(max_length=200)),
                ('book', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='textbook_app.book')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='textbook_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='textbook_app.book')),
                ('borrower', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='textbook_app.user')),
                ('ownedbook', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='textbook_app.ownedbook')),
            ],
        ),
    ]
