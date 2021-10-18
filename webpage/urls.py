from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="initial"),
    path("home", views.IndexView.as_view(), name="home"),
    path("biomarker-comparison", views.BiomarkerComparisonView.as_view(), name="biomarker-comparison"),
    path("patients", views.PatientsView.as_view(), name="patients"),
    path("about-us", views.AboutUsView.as_view(), name="about-us"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("signup", views.signupView, name="signup"),
    path("donate", views.DonateView.as_view(), name="donate"),
    path("privacy-policy", views.PrivacyPolicyView.as_view(), name="privacy-policy"),
    path("<int:pk>/edit-profile", views.EditProfilePageView.as_view(), name="edit-profile"),
]
