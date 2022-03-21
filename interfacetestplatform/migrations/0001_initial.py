# Generated by Django 2.0.2 on 2022-03-10 18:15

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseSuite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('suite_desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='用例集合描述')),
                ('if_execute', models.IntegerField(default=0, help_text='0：执行；1：不执行', verbose_name='是否执行')),
                ('test_case_model', models.CharField(blank=True, help_text='data/keyword', max_length=100, null=True, verbose_name='测试执行模式')),
                ('creator', models.CharField(blank=True, max_length=50, null=True)),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用例集合表',
                'verbose_name_plural': '用例集合表',
            },
        ),
        migrations.CreateModel(
            name='CaseSuiteExecuteRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('run_time_interval', models.IntegerField(default=0, null=True, verbose_name='延迟时间')),
                ('status', models.IntegerField(default=0, null=True, verbose_name='执行状态')),
                ('test_result', models.CharField(blank=True, max_length=50, null=True)),
                ('creator', models.CharField(blank=True, max_length=50, null=True)),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('execute_start_time', models.CharField(blank=True, max_length=300, null=True, verbose_name='执行开始时间')),
                ('case_suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interfacetestplatform.CaseSuite', verbose_name='测试集合')),
            ],
        ),
        migrations.CreateModel(
            name='CaseSuiteTestCaseExecuteRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=0, null=True, verbose_name='执行状态')),
                ('exception_info', models.CharField(blank=True, max_length=2048, null=True)),
                ('request_data', models.CharField(max_length=1024, null=True, verbose_name='请求体')),
                ('response_data', models.CharField(max_length=1024, null=True, verbose_name='响应字符串')),
                ('execute_result', models.CharField(max_length=1024, null=True, verbose_name='执行结果')),
                ('extract_var', models.CharField(max_length=1024, null=True, verbose_name='关联参数')),
                ('last_time_response_data', models.CharField(max_length=1024, null=True, verbose_name='上一次响应字符串')),
                ('execute_total_time', models.CharField(max_length=1024, null=True, verbose_name='执行耗时')),
                ('execute_start_time', models.CharField(blank=True, max_length=300, null=True, verbose_name='执行开始时间')),
                ('execute_end_time', models.CharField(blank=True, max_length=300, null=True, verbose_name='执行结束时间')),
                ('case_suite_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interfacetestplatform.CaseSuiteExecuteRecord', verbose_name='测试集合执行记录')),
            ],
        ),
        migrations.CreateModel(
            name='InterfaceServer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('env', models.CharField(default='', max_length=50, verbose_name='环境')),
                ('ip', models.CharField(default='', max_length=50, verbose_name='ip')),
                ('port', models.CharField(default='', max_length=100, verbose_name='端口')),
                ('remark', models.CharField(max_length=100, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '接口地址配置表',
                'verbose_name_plural': '接口地址配置表',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='模块名称')),
                ('test_owner', models.CharField(max_length=50, verbose_name='测试负责人')),
                ('desc', models.CharField(max_length=100, null=True, verbose_name='简要描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '模块信息表',
                'verbose_name_plural': '模块信息表',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='项目名称')),
                ('proj_owner', models.CharField(max_length=20, verbose_name='项目负责人')),
                ('test_owner', models.CharField(max_length=20, verbose_name='测试负责人')),
                ('dev_owner', models.CharField(max_length=20, verbose_name='开发负责人')),
                ('desc', models.CharField(max_length=100, null=True, verbose_name='项目描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='项目创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='项目更新时间')),
            ],
            options={
                'verbose_name': '项目信息表',
                'verbose_name_plural': '项目信息表',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrname', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='SuiteCase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=1, help_text='0：有效，1：无效', verbose_name='是否有效')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('case_suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interfacetestplatform.CaseSuite', verbose_name='用例集合')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('case_name', models.CharField(max_length=50, verbose_name='用例名称')),
                ('request_data', models.CharField(default='', max_length=1024, verbose_name='请求数据')),
                ('uri', models.CharField(default='', max_length=1024, verbose_name='接口地址')),
                ('assert_key', models.CharField(max_length=1024, null=True, verbose_name='断言内容')),
                ('maintainer', models.CharField(default='', max_length=1024, verbose_name='编写人员')),
                ('extract_var', models.CharField(max_length=1024, null=True, verbose_name='提取变量表达式')),
                ('request_method', models.CharField(max_length=1024, null=True, verbose_name='请求方式')),
                ('status', models.IntegerField(help_text='0：表示有效，1：表示无效，用于软删除', null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('belong_module', smart_selects.db_fields.GroupedForeignKey(group_field='belong_project', on_delete=django.db.models.deletion.CASCADE, to='interfacetestplatform.Module', verbose_name='所属模块')),
                ('belong_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interfacetestplatform.Project', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '测试用例表',
                'verbose_name_plural': '测试用例表',
            },
        ),
        migrations.CreateModel(
            name='TestCaseExecuteResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(help_text='0：表示未执行，1：表示已执行', null=True)),
                ('exception_info', models.CharField(blank=True, max_length=2048, null=True)),
                ('request_data', models.CharField(max_length=1024, null=True, verbose_name='请求体')),
                ('response_data', models.CharField(max_length=1024, null=True, verbose_name='响应字符串')),
                ('execute_result', models.CharField(max_length=1024, null=True, verbose_name='执行结果')),
                ('extract_var', models.CharField(max_length=1024, null=True, verbose_name='关联参数')),
                ('last_time_response_data', models.CharField(max_length=1024, null=True, verbose_name='上一次响应字符串')),
                ('execute_total_time', models.CharField(max_length=1024, null=True, verbose_name='执行耗时')),
                ('execute_start_time', models.CharField(blank=True, max_length=300, null=True, verbose_name='执行开始时间')),
                ('execute_end_time', models.CharField(blank=True, max_length=300, null=True, verbose_name='执行结束时间')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('belong_test_case', smart_selects.db_fields.GroupedForeignKey(group_field='belong_test_case', on_delete=django.db.models.deletion.CASCADE, to='interfacetestplatform.TestCase', verbose_name='所属用例')),
            ],
            options={
                'verbose_name': '用例执行结果记录表',
                'verbose_name_plural': '用例执行结果记录表',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['c_time'],
            },
        ),
        migrations.AddField(
            model_name='testcase',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='interfacetestplatform.User', verbose_name='责任人'),
        ),
        migrations.AddField(
            model_name='suitecase',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interfacetestplatform.TestCase', verbose_name='测试用例'),
        ),
        migrations.AddField(
            model_name='module',
            name='belong_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interfacetestplatform.Project'),
        ),
        migrations.AddField(
            model_name='casesuitetestcaseexecuterecord',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interfacetestplatform.TestCase', verbose_name='测试用例'),
        ),
    ]
