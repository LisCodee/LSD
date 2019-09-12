# Generated by Django 2.2.5 on 2019-09-07 03:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False, verbose_name='留言id')),
                ('project_id', models.IntegerField(verbose_name='项目的id')),
                ('read', models.IntegerField(default=0, verbose_name='是否已读')),
                ('effective', models.IntegerField(default=0, verbose_name='是否有效')),
                ('time', models.DateField(default=django.utils.timezone.now, verbose_name='时间')),
                ('content', models.CharField(max_length=256, null=True, verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False, verbose_name='项目id，自增')),
                ('project_name', models.CharField(max_length=20, verbose_name='项目名称')),
                ('source', models.CharField(max_length=30, verbose_name='项目来源')),
                ('contacts', models.CharField(max_length=20, verbose_name='对方联系人')),
                ('telephone', models.CharField(max_length=20, verbose_name='联系电话')),
                ('introduction', models.CharField(max_length=256, verbose_name='项目简介')),
                ('time', models.DateField(default=django.utils.timezone.now, verbose_name='时间')),
                ('effective', models.IntegerField(default=0, verbose_name='是否有效')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(max_length=32, verbose_name='汇报标题')),
                ('project_id', models.IntegerField(verbose_name='所属项目id')),
                ('reporter', models.CharField(max_length=20, verbose_name='汇报人')),
                ('capital', models.CharField(max_length=256, verbose_name='资金情况')),
                ('workable', models.CharField(max_length=1024, verbose_name='落实情况')),
                ('invoice', models.CharField(max_length=256, verbose_name='开票情况')),
                ('progress', models.CharField(max_length=1024, verbose_name='项目进展')),
                ('supply', models.CharField(max_length=1024, verbose_name='供货情况')),
                ('other', models.CharField(max_length=1024, verbose_name='其它')),
                ('effective', models.IntegerField(default=0, verbose_name='是否有效')),
                ('time', models.DateField(default=django.utils.timezone.now, verbose_name='时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=16, unique=True, verbose_name='用户名即真实姓名')),
                ('password', models.CharField(max_length=32, verbose_name='密码+MD5加密')),
                ('telephone', models.CharField(max_length=20, null=True, verbose_name='电话')),
                ('authority', models.CharField(default='salesman', max_length=20, verbose_name='权限')),
            ],
        ),
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=16, verbose_name='业务员姓名')),
                ('project_id', models.CharField(max_length=20, verbose_name='项目名称')),
            ],
        ),
        migrations.CreateModel(
            name='UserStr',
            fields=[
                ('userStr_id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('user_name', models.CharField(max_length=16, unique=True, verbose_name='用户名称')),
                ('str', models.CharField(max_length=10, verbose_name='加密字符串')),
            ],
        ),
    ]
