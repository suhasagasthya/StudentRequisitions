# Generated by Django 2.1 on 2018-12-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20181215_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisitions',
            name='id',
        ),
        migrations.AddField(
            model_name='requisitions',
            name='reqid',
            field=models.CharField(default='adsc001', max_length=7, primary_key=True, serialize=False),
        ),
    ]
