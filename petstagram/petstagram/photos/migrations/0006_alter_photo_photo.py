# Generated by Django 4.2.4 on 2024-03-26 08:52

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='mediafiles/pet_photos/', validators=[petstagram.photos.validators.validate_file_less_than_5mb]),
        ),
    ]
