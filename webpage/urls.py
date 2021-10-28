from django.contrib import admin
from django.urls import path
from . import views

app_name = 'webpage'

urlpatterns = [
    path("", views.IndexView.as_view(), name="initial"),
    path("home", views.IndexView.as_view(), name="home"),
    path("biomarker-comparison", views.BiomarkerComparisonView.as_view(), name="biomarker-comparison"),
    path("<int:pk>/medical-information", views.MedicalInformationView.as_view(), name="medical-information"),
    path("medical-information", views.MedicalInformationNoLoginView.as_view(), name="medical-information-nologin"),
    path("about-us", views.AboutUsView.as_view(), name="about-us"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("signup", views.signupView, name="signup"),
    path("donate", views.DonateView.as_view(), name="donate"),
    path("privacy-policy", views.PrivacyPolicyView.as_view(), name="privacy-policy"),
    path("<int:pk>/show-profile", views.ShowProfilePageView.as_view(), name="show-profile"),
    path("<int:pk>/edit-profile", views.EditProfilePageView.as_view(), name="edit-profile"),
]
