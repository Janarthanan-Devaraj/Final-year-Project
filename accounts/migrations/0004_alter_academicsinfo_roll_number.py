# Generated by Django 4.1.7 on 2023-02-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicsinfo',
            name='roll_number',
            field=models.CharField(blank=True, max_length=7, unique=True),
        ),
    ]