# Generated by Django 5.0 on 2024-01-02 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customers_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='customers_h',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('Adharcard_no', models.IntegerField()),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='customers',
        ),
    ]
