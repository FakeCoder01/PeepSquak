# Generated by Django 4.1.2 on 2022-10-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_words_desc_alter_words_pronunciation'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150)),
                ('msg', models.TextField()),
            ],
        ),
    ]