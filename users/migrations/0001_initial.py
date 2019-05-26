# Generated by Django 2.2.1 on 2019-05-26 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('chat_id', models.CharField(max_length=16, unique=True)),
                ('name', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_friend', related_query_name='friend_friends', to='users.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_user', related_query_name='friend_users', to='users.User')),
            ],
            options={
                'unique_together': {('user', 'friend')},
            },
        ),
    ]
