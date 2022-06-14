# Generated by Django 4.0.5 on 2022-06-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_skills_skill_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(help_text='Enter a Skill', max_length=250),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_rating',
            field=models.CharField(help_text=' Choose between: excellent,very-good,good,beginner', max_length=250),
        ),
    ]
