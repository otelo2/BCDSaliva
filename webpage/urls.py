from django.urls import path
from . import views

urlpatterns = [
    path("", views.SiteView.as_view()),
]
