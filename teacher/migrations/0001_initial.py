# Generated by Django 4.1.2 on 2022-11-21 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='t-avatar.jpg', null=True, upload_to='teachers/')),
                ('full_name', models.CharField(default='', max_length=50, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('gender', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('address', models.TextField(blank=True, default='', null=True)),
                ('zipcode', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('psw', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('classroom', models.ManyToManyField(blank=True, null=True, related_name='classroommodel', to='school.classroom')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schoolprofile', to='school.school')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacherprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]