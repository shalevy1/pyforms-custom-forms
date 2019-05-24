# Generated by Django 2.2 on 2019-05-23 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=255, verbose_name='Name')),
                ('active', models.BooleanField(verbose_name='Active')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='FormTypeFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_label', models.CharField(max_length=255, verbose_name='Field label')),
                ('field_type', models.CharField(choices=[('ControlText', 'Small text'), ('ControlCheckbox', 'Check box')], max_length=50, verbose_name='Field type')),
                ('form_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_extra_fields.FormType')),
            ],
        ),
    ]