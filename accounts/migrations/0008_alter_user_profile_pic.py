# Generated by Django 4.1.7 on 2023-02-23 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default-img.png', null=True, upload_to='profile_pics'),
        ),
    ]
