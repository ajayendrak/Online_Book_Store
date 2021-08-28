# Generated by Django 3.2.3 on 2021-08-28 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeowner', '0003_auto_20210827_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('bookid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('storename', models.CharField(max_length=50)),
                ('bookname', models.CharField(max_length=50)),
                ('bookprice', models.IntegerField(default=1)),
                ('bookauthor', models.CharField(max_length=50)),
                ('bookimage', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
    ]