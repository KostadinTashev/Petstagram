from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

from petstagram.core.model_mixins import StrFromFieldsMixin
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_less_than_5mb


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'location')
    MIN_LENGTH_DESCRIPTION = 10
    MAX_LENGTH_DESCRIPTION = 300
    MAX_LENGTH_LOCATION = 30

    photo = models.ImageField(
        upload_to='mediafiles/pet_photos/',
        validators=(validate_file_less_than_5mb,),
        null=False,
        blank=True,
    )

    description = models.CharField(
        max_length=MAX_LENGTH_DESCRIPTION,
        validators=(validators.MinLengthValidator(MIN_LENGTH_DESCRIPTION),),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LENGTH_LOCATION,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    # One-to-one relations
    # One-to-many relations
    # Many-to-many relations

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
