from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
# Source: https://stackoverflow.com/questions/57918725/how-to-extend-django-usercreationform-model-to-include-phone-number-field
class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname_1 = models.CharField(max_length=50)
    surname_2 = models.CharField(blank=True, max_length=50)
    date_of_birth = models.DateField(null=True, max_length=13)
    gender = models.CharField(max_length=7)
    level_of_education = models.CharField(max_length=9)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    monthly_income = models.CharField(max_length=21)
    phone_regex = RegexValidator(regex=r'\(\d\d\d\)\ \d\d\d\ \-\ \d\d\d\d', message="Phone number must be entered in the format: '(123) 123 - 1234'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    #phone_number = PhoneNumberField()

class UserFile(models.Model):
    # Store the path of the file in the db and the file will be on the hard drive
    # File will be stored in the folder "files" in the DIR selected in settings.py
    file = models.FileField(upload_to="files")
