# Generated by Django 3.2.4 on 2021-06-14 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='category',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='forums',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Forum',
        ),
    ]
