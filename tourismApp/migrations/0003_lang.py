# Generated by Django 3.2.6 on 2021-10-17 14:19

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourismApp', '0002_crowding_logcrowd_logvc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.OneToOneField(db_column=builtins.id, on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tourismApp.delang')),
                ('code_html', models.CharField(max_length=16384)),
                ('active', models.BooleanField()),
            ],
            options={
                'db_table': 'lang',
                'managed': False,
            },
        ),
    ]