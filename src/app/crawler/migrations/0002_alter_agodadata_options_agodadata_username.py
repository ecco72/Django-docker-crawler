# Generated by Django 4.2.13 on 2024-06-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agodadata',
            options={'ordering': ['price'], 'verbose_name': '訂房網站資料', 'verbose_name_plural': '訂房網站資料集'},
        ),
        migrations.AddField(
            model_name='agodadata',
            name='username',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
    ]
