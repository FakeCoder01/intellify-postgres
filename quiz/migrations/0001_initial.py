# Generated by Django 4.1.2 on 2022-11-03 11:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('teacher', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.CharField(max_length=300)),
                ('is_correct', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=500)),
                ('marks', models.IntegerField(default=1)),
                ('standard', models.CharField(blank=True, max_length=50, null=True)),
                ('chapter', models.CharField(blank=True, max_length=200, null=True)),
                ('topic', models.CharField(blank=True, max_length=200, null=True)),
                ('tags', models.CharField(blank=True, max_length=1000, null=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level', to='quiz.category')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.subjects')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('quiz_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('quiz_schedule', models.DateTimeField(default=datetime.datetime(2022, 11, 3, 18, 39, 20, 40410))),
                ('time_limit', models.IntegerField(blank=True, null=True)),
                ('no_of_questions', models.IntegerField(blank=True, null=True)),
                ('quiz_number', models.IntegerField(blank=True, null=True)),
                ('quiz_type', models.CharField(blank=True, max_length=50, null=True)),
                ('allowed_atempts', models.IntegerField(blank=True, default=1, null=True)),
                ('title', models.CharField(max_length=256)),
                ('student_list', models.TextField(blank=True, null=True)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_classroom', to='school.classroom')),
                ('question_list', models.ManyToManyField(blank=True, null=True, to='quiz.question')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.subjects')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher_profile')),
            ],
        ),
        migrations.CreateModel(
            name='quiz_response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluate', models.IntegerField(default=0)),
                ('quiz_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=50)),
                ('teacher_name', models.CharField(max_length=50)),
                ('answer_text', models.CharField(max_length=50)),
                ('correct_answer_text', models.CharField(max_length=50)),
                ('question_text', models.CharField(max_length=150)),
                ('question_tags', models.CharField(max_length=150)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('correct_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='correct_answer_quizresponse', to='quiz.answer')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_quizresponse', to='quiz.question')),
                ('quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_quizresponse', to='quiz.quiz')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_quizresponse', to='student.student_profile')),
                ('student_answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_quizresponse', to='quiz.answer')),
            ],
        ),
        migrations.CreateModel(
            name='quiz_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.CharField(blank=True, default='0', max_length=5, null=True)),
                ('attempted_question', models.IntegerField(default=0)),
                ('submited_on', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_quizmaster', to='quiz.quiz')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_quizmaster', to='student.student_profile')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='quiz.question'),
        ),
    ]
