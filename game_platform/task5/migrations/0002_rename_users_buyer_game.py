# Generated by Django 4.2.14 on 2024-08-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task5', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Buyer',
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('size', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
                ('age_limited', models.BooleanField(verbose_name=True)),
                ('buyer', models.ManyToManyField(related_name='buyer', to='task5.buyer')),
            ],
        ),
    ]