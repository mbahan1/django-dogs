# Generated by Django 4.0.3 on 2022-03-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_dogtoy_alter_dog_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='dogtoys',
            field=models.ManyToManyField(to='main_app.dogtoy'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='gender',
            field=models.CharField(choices=[('f', 'female'), ('m', 'male')], max_length=10),
        ),
    ]