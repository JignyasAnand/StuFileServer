# Generated by Django 4.1.7 on 2023-02-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LFiles', '0002_urlval'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlConts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('conts', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='UrlVal',
        ),
    ]
