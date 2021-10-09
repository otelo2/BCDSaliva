from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="initial"),
    path("home", views.IndexView.as_view(), name="home"),
    path("biomarker-comparison", views.BiomarkerComparisonView.as_view(), name="biomarker-comparison"),
    path("patients", views.PatientsView.as_view(), name="patients"),
    path("about-us", views.AboutUsView.as_view(), name="about-us"),
    path("login", views.LoginView.as_view(), name="login"),
    path("signup", views.SignupView.as_view(), name="signup"),
    path("donate", views.DonateView.as_view(), name="donate"),
    path("privacy-policy", views.PrivacyPolicyView.as_view(), name="privacy-policy"),
]
