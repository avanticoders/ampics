# Generated by Django 4.0.3 on 2022-03-30 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_account_downloads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.account'),
        ),
    ]
