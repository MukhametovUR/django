# Generated by Django 4.2.1 on 2023-12-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('altrum', '0003_alter_altrum_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altrum',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0),
        ),
    ]
