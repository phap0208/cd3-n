# Generated by Django 4.2.6 on 2023-10-10 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0023_alter_test_start_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='test',
            new_name='test_belongs_to',
        ),
        migrations.AddField(
            model_name='test',
            name='current_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_questions', to='authentication.question'),
        ),
        migrations.AlterField(
            model_name='test',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]