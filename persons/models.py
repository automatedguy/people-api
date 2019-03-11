from django.db import models
from model_utils import Choices


class Person(models.Model):

    user_name = models.CharField(max_length=15, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    creation_date = models.DateField()
    active = models.BooleanField()
    SEX = Choices('M', 'F')
    sex = models.CharField(choices=SEX, default=SEX.M, max_length=1)

    class Meta:
        db_table = '"person"'

    def __str__(self):
        return self.user_name


class ContactInfo(models.Model):
    pass

    class Meta:
        db_table = '"contact_info"'


class LocationInfo(models.Model):
    pass

    class Meta:
        db_table = '"location_info"'


class Presentation(models.Model):
    pass

    class Meta:
        db_table = '"presentation"'


class Description(models.Model):
    pass

    class Meta:
        db_table = '"description"'


class Review(models.Model):
    pass

    class Meta:
        db_table = '"review"'


class Photos(models.Model):
    pass

    class Meta:
        db_table = '"photos"'


class Videos(models.Model):
    pass

    class Meta:
        db_table = '"video"'
