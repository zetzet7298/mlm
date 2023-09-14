# Generated by Django 4.2 on 2023-07-10 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=128, unique=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.menu')),
            ],
            options={
                'db_table': 'menu',
            },
        ),
    ]
