# Generated by Django 2.0 on 2017-12-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('author', models.CharField(blank=True, default='', max_length=20)),
                ('pw', models.CharField(blank=True, default='', max_length=12)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
