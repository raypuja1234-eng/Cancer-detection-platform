
from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path("",myapp.views.home),
    path("about/",myapp.views.about),
    path("contact/",myapp.views.contact),
    path("analysis/",myapp.views.analysis),
    path("ourteam/",myapp.views.ourteam),
    path("prediction/",myapp.views.prediction),
    path("pred/",myapp.views.pred),
]
