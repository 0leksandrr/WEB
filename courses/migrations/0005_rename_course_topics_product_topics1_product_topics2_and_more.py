# Generated by Django 5.0 on 2023-12-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_product_course_topics_product_course_topics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='course_topics',
            new_name='topics1',
        ),
        migrations.AddField(
            model_name='product',
            name='topics2',
            field=models.TextField(default='wqwe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='topics3',
            field=models.TextField(default='wqwe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='topics4',
            field=models.TextField(default='wqwe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='topics5',
            field=models.TextField(default='wqwe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='topics6',
            field=models.TextField(default='wqwe'),
            preserve_default=False,
        ),
    ]