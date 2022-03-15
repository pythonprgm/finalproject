# Generated by Django 3.2.12 on 2022-03-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personaldetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('email', models.TextField()),
                ('phonenumber', models.IntegerField()),
                ('billingaddress', models.TextField()),
                ('youradress', models.TextField()),
                ('state', models.TextField()),
                ('district', models.TextField()),
                ('subdistrict', models.TextField()),
            ],
        ),
    ]