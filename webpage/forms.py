from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


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
class CreateUserForm(UserCreationForm):
    name = forms.CharField()
    surname_1 = forms.CharField()
    surname_2 = forms.CharField(required=False, label="Surname 2 (Optional)")
    date_of_birth = forms.DateField(widget=DateInput)
    gender = forms.ChoiceField(choices=GENDER_CHOICES) #Wont work
    level_of_education = forms.ChoiceField(choices=LEVEL_OF_EDUCATION_CHOICES)
    country = forms.CharField()
    state = forms.CharField()
    ocupation = forms.CharField()
    monthly_income = forms.ChoiceField(choices=MONTHLY_INCOME_CHOICES)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["name", "surname_1", "surname_2", "date_of_birth", "gender", \
                  "level_of_education", "country", "state", "ocupation", \
                  "monthly_income", "email", "password1", "password2"]
