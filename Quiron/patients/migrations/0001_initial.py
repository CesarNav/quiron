# Generated by Django 3.1.3 on 2020-11-25 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(choices=[('CC', 'Cedula Ciudadania'), ('CE', 'Cedula Extranjeria'), ('TI', 'Tarjeta Identidad')], max_length=2)),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('age', models.IntegerField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('civilState', models.CharField(blank=True, max_length=10, null=True)),
                ('ocupation', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone', models.CharField(max_length=10)),
                ('adress', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
