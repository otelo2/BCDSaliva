from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import PatientProfile

class UploadFileForm(forms.Form):
    uploaded_file = forms.FileField()
    
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
)
LEVEL_OF_EDUCATION_CHOICES = (
    ("Basic", "Elementary school"),
    ("Middle", "Secondary school / Highschool"),
    ("Upper", "University"),
    ("Postgrad", "Postgraduate")
)
MONTHLY_INCOME_CHOICES = (
    ("Poverty", "Less than $20,000"),
    ("Low income", "$20,000 - $44,999"),
    ("Middle class", "$45,000 - $139,999"),
    ("Upper middle class", "$149,000 - $149,999"),
    ("High income", "$150,000 - $199,999"),
    ("Highest tax brackets", "More than $200,000")
)

class DateInput(forms.DateInput):
    input_type = "date"
class CreatePatientForm(forms.ModelForm):
    name = forms.CharField()
    surname_1 = forms.CharField()
    surname_2 = forms.CharField(required=False, label="Surname 2 (Optional)")
    date_of_birth = forms.DateField(widget=DateInput)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    level_of_education = forms.ChoiceField(choices=LEVEL_OF_EDUCATION_CHOICES)
    country = forms.CharField()
    state = forms.CharField()
    occupation = forms.CharField()
    monthly_income = forms.ChoiceField(choices=MONTHLY_INCOME_CHOICES)
    phone_number = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'\(\d\d\d\)\ \d\d\d\ \-\ \d\d\d\d', 'title':'Phone number must be entered in the format: "(123) 123 - 1234".'}))
    class Meta:
        model = PatientProfile
        fields = ["name", "surname_1", "surname_2", "date_of_birth", "gender", \
                  "level_of_education", "country", "state", "occupation", \
                  "monthly_income", "phone_number"]
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]