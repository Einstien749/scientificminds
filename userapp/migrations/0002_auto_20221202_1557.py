# Generated by Django 2.1 on 2022-12-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(default='userimages/def.jpg', upload_to='userimage'),
        ),
    ]
