# Generated by Django 4.0 on 2022-01-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0003_alter_user_address_alter_user_kakao_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='item_condition',
            field=models.CharField(choices=[('새제품', '새제품'), ('최상', '최상'), ('상', '상'), ('중', '중'), ('하', '하')], max_length=5),
        ),
    ]
