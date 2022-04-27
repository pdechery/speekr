# Generated by Django 4.0.3 on 2022-03-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speekr', '0004_alter_user_friends'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterModelOptions(
            name='quote',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterModelOptions(
            name='repost',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='repost',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]