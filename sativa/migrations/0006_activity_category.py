# Generated by Django 5.1.1 on 2024-10-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sativa', '0005_spapricing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.CharField(choices=[('family_fun', 'Family Fun'), ('kids_playground', 'Kids Playground')], default='family_fun', max_length=100),
        ),
    ]