# Generated by Django 4.0.2 on 2022-02-28 13:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_alter_expense_options_alter_expense_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 13, 45, 23, 612224, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expensedetail',
            name='expense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense_detail', to='expense.expense'),
        ),
    ]
