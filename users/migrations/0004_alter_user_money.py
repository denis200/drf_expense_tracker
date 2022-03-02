# Generated by Django 4.0.2 on 2022-03-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]