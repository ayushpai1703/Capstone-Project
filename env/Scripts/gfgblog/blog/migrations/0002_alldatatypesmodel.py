# Generated by Django 5.0.6 on 2024-06-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllDataTypesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_text', models.CharField(max_length=100)),
                ('long_text', models.TextField()),
                ('integer_number', models.IntegerField()),
                ('float_number', models.FloatField()),
                ('decimal_number', models.DecimalField(decimal_places=2, max_digits=10)),
                ('boolean_field', models.BooleanField()),
                ('date_field', models.DateField()),
                ('time_field', models.TimeField()),
                ('datetime_field', models.DateTimeField()),
                ('file_field', models.FileField(upload_to='uploads/')),
                ('image_field', models.ImageField(upload_to='uploads/images/')),
                ('email_field', models.EmailField(max_length=254)),
                ('url_field', models.URLField()),
                ('json_field', models.JSONField()),
                ('uuid_field', models.UUIDField()),
                ('related_models', models.ManyToManyField(blank=True, to='blog.alldatatypesmodel')),
            ],
        ),
    ]
