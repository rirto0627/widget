# Generated by Django 3.0.8 on 2020-07-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='front',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('photo', models.URLField(blank=True)),
                ('location', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('Sex', models.CharField(choices=[(0, '男'), (1, '女')], default=0, max_length=2)),
                ('Language', models.CharField(choices=[(0, '繁體中文'), (1, '英文')], default=0, max_length=2)),
            ],
        ),
    ]