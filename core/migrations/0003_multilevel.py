# Generated by Django 4.2 on 2023-09-13 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_menu_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.multilevel')),
            ],
            options={
                'db_table': 'multi_level',
            },
        ),
    ]
