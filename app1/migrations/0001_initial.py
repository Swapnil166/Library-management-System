# Generated by Django 3.2.9 on 2021-11-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('bookname', models.CharField(max_length=50, unique=True)),
                ('bookid', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('password2', models.CharField(max_length=50, null=True)),
                ('fname', models.CharField(max_length=50, null=True)),
                ('lname', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]