# Generated by Django 3.2.16 on 2023-01-24 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0001_initial'),
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='disciplina_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disciplina.disciplina'),
        ),
    ]
