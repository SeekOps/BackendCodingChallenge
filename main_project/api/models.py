from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    User model extending django's Abstract User
    '''
    company = models.ForeignKey('Company', related_name='user',
                                on_delete=models.CASCADE)
    can_login = models.BooleanField(default=False)
    preferences = models.CharField(max_length=128, null=True)

    def __str__(self):
        return


class Company(models.Model):
    name = models.CharField(max_length=128)
    customer = models.BooleanField(default=True)
    address = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    serial_number = models.CharField(max_length=30)

    def __str__(self):
        return f'Sensor {self.serial_number}'


class Inspection(models.Model):
    '''
    Model that stores information about a site inspection.

    An operator goes to site and inspects the site using a
    sensor. The sensor takes measurements of physical properties
    at the location.

    Required fields:

        location (name of a location)
        company (relates to company object)
        sensor (relates to sensor object)
        start_time
        deleted (true or false for a 'soft delete' functionality)
        operator (the user who performed the inspection)
    '''
    pass


class Measurement(models.Model):
    '''
    Atomic measurement taken by a sensor. This object specifies the
    time, location and measurement value.

    concentration is saved as parts per million
    temperature is saved in degrees Kelvin
    pressure is saved in bars

    Required Fields:

        time 
        inspection (relates to inspection object)
        concentration
        latitude
        longitude 
        temperature
        pressure 
    '''
    pass
