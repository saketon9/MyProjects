# Generated by Django 3.1.1 on 2020-11-11 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobready', '0003_auto_20201008_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=500)),
                ('review_Category', models.CharField(choices=[('G', 'Google'), ('F', 'Facebook'), ('kh', 'Khoros')], default='Not Available', max_length=50)),
            ],
        ),
    ]
