# Generated by Django 3.2.16 on 2022-11-01 19:46

import bookwyrm.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0164_merge_0159_auto_20220924_0634_0163_genre_remote_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinimumVotesSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_genre_votes', models.IntegerField(default=10)),
                ('minimum_book_votes', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='SuggestedGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', bookwyrm.models.fields.CharField(max_length=40)),
                ('description', bookwyrm.models.fields.CharField(max_length=500)),
                ('votes', bookwyrm.models.fields.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SuggestedBookGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', bookwyrm.models.fields.IntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookwyrm.work')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookwyrm.genre')),
            ],
        ),
    ]