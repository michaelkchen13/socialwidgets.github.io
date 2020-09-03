# Generated by Django 3.0.3 on 2020-04-24 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialWidgets', '0007_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='image',
            new_name='profileImage',
        ),
        migrations.AddField(
            model_name='user',
            name='imgFilter',
            field=models.CharField(default='noFilter', max_length=50),
        ),
    ]