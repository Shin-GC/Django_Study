# Generated by Django 4.0 on 2022-01-09 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0003_review_alter_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coplate.user'),
            preserve_default=False,
        ),
    ]
