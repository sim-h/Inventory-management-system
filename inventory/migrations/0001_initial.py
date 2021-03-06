# Generated by Django 2.2 on 2019-04-28 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('mean', models.FloatField(default=0.0)),
                ('sd', models.FloatField(default=0.0)),
                ('price', models.FloatField(default=0.0)),
                ('holding_cost', models.FloatField(default=0.0)),
                ('ordering_cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OtherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('lead_time', models.FloatField(default=0.0)),
                ('sd', models.FloatField(default=0.0)),
                ('content_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'inventory'), ('model', 'centre')), models.Q(('app_label', 'inventory'), ('model', 'supplier')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Medicine')),
            ],
            options={
                'index_together': {('content_type', 'object_id')},
            },
        ),
    ]
