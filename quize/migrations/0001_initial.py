# Generated by Django 5.0.3 on 2024-03-23 12:49

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quize.question')),
            ],
        ),
        migrations.CreateModel(
            name='Question_Set',
            fields=[
                ('qs_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('level', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Difficult', 'Difficult'), ('Hard', 'Hard')], default='Easy', max_length=10)),
                ('time_set', models.PositiveSmallIntegerField(default=5)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Question_Sets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='qs_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quize.question_set'),
        ),
        migrations.CreateModel(
            name='Studen_Result',
            fields=[
                ('result_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('score', models.FloatField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('qs_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quize.question_set')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Subject',
            fields=[
                ('sub_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]