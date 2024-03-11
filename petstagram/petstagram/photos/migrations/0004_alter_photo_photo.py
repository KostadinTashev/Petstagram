# Generated by Django 4.2.4 on 2024-03-11 17:34

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_tagged_pets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='mediafiles/pet_photos/', validators=[petstagram.photos.validators.validate_file_less_than_5mb]),
        ),
    ]
