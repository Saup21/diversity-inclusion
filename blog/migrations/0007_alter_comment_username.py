# Generated by Django 3.2.3 on 2021-05-28 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(blank=True, max_length=112, null=True),
        ),
    ]