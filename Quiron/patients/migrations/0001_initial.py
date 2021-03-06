# Generated by Django 3.1.3 on 2020-12-09 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('name', models.CharField(default=None, max_length=60)),
                ('last_name', models.CharField(default=None, max_length=60)),
                ('id_type', models.CharField(choices=[('CC', 'Cedula Ciudadania'), ('CE', 'Cedula Extranjeria'), ('PE', 'Pasaporte')], default=None, max_length=2)),
                ('id_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date_birth', models.DateField(default=None)),
                ('age', models.IntegerField(blank=True, default=None)),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default=None, max_length=1)),
                ('civil_state', models.CharField(choices=[('Soltero/a', 'Soltero/a'), ('Casado/a', 'Casado/a'), ('Union libre', 'Union libre'), ('Divorciado/a', 'Divorciado/a'), ('Viudo/a', 'Viudo/a')], default=None, max_length=12)),
                ('ocupation', models.CharField(blank=True, max_length=20, null=True)),
                ('schoolarchip', models.CharField(choices=[('Sin escolaridad', 'Sin escolaridad'), ('Primaria', 'Primaria'), ('Secundaria', 'Secundaria'), ('Pregrado', 'Pregrado'), ('Postgrado', 'Postgrado')], default=None, max_length=20)),
                ('telephone', models.CharField(max_length=10)),
                ('adress', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('status', models.CharField(choices=[('A', 'Activate'), ('D', 'Deactivate')], default='A', max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('used_techniques', models.CharField(max_length=200)),
                ('conclusions', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
    ]
