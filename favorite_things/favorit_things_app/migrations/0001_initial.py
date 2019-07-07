# Generated by Django 2.2.3 on 2019-07-07 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteThing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('ranking', models.IntegerField()),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date_time', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='favorit_things_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='AuditTrail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('column_changed', models.CharField(max_length=30)),
                ('old_value', models.CharField(max_length=100)),
                ('new_value', models.CharField(max_length=100)),
                ('modified_date_time', models.DateTimeField()),
                ('favorite_thing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='favorit_things_app.FavoriteThing')),
            ],
        ),
    ]
