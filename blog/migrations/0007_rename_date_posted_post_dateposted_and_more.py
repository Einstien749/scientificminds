# Generated by Django 4.1.3 on 2022-12-15 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_category_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_posted',
            new_name='dateposted',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_img',
            new_name='postimg',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_url',
            new_name='posturl',
        ),
    ]
