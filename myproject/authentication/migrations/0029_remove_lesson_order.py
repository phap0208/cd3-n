# Generated by Django 4.2.6 on 2023-10-20 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0028_remove_test_course_test_lesson_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='order',
        ),
    ]
