# Generated by Django 3.2.9 on 2021-11-17 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_remove_entry_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagedge',
            name='child',
        ),
        migrations.RemoveField(
            model_name='tagedge',
            name='parent',
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='tracker.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='associated_tags',
            field=models.ManyToManyField(to='tracker.Tag'),
        ),
        migrations.DeleteModel(
            name='EntryTag',
        ),
        migrations.DeleteModel(
            name='TagEdge',
        ),
    ]