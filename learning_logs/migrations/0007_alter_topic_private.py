# Generated by Django 3.2.5 on 2021-07-22 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0006_topic_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='private',
            field=models.BooleanField(verbose_name='Privado'),
        ),
    ]
