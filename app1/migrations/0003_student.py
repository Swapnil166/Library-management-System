# Generated by Django 3.2.9 on 2021-11-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_user_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('password2', models.CharField(max_length=50, null=True)),
                ('fname', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
