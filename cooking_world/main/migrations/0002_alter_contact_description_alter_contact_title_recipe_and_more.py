# Generated by Django 4.0.3 on 2022-04-11 21:38

import cooking_world.common.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(max_length=400, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5), cooking_world.common.validators.validate_only_letters]),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5), cooking_world.common.validators.validate_only_letters])),
                ('photo', models.ImageField(upload_to='recipe/', validators=[cooking_world.common.validators.MaxFileSizeInMbValidator(5)])),
                ('cuisine', models.CharField(choices=[('FRENCH', 'French'), ('ITALIAN', 'Italian'), ('BULGARIAN', 'Bulgarian'), ('CHINESE', 'Chinese'), ('GREEK', 'Greek'), ('JAPANESE', 'Japanese'), ('INDIAN', 'Indian'), ('SPANISH', 'Spanish'), ('MOROCCAN', 'Moroccan'), ('LEBANESE', 'Lebanese'), ('MEDITERRANEAN', 'Mediterranean'), ('TURKISH', 'Turkish'), ('THAI', 'Thai')], max_length=13)),
                ('meal_type', models.CharField(choices=[('BREAKFAST', 'Breakfast'), ('STARTER', 'Starter'), ('LUNCH', 'Lunch'), ('DINNER', 'Dinner'), ('DESSERT', 'Dessert')], max_length=9)),
                ('dificulty', models.CharField(choices=[('NOVICE', 'Novice'), ('ADVANCED', 'Advanced'), ('EXPERT', 'Expert')], max_length=8)),
                ('preparation_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cooking_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('servings', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('description', models.TextField(max_length=3000, validators=[django.core.validators.MinLengthValidator(5)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5), cooking_world.common.validators.validate_only_letters])),
                ('photo', models.ImageField(upload_to='blog/', validators=[cooking_world.common.validators.MaxFileSizeInMbValidator(5)])),
                ('description', models.TextField(max_length=5000, validators=[django.core.validators.MinLengthValidator(5)])),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]