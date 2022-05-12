from unicodedata import name
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

urlpatterns = [
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('patients/', views.patients, name = "patients"),
    path('doctors/', views.doctors, name = "doctors"),
    path('patients/<int:id>/', views.patient, name = "patient"),
    path('report/<int:id>', views.report, name = "report"),
    path('addpatient/', views.addpatient, name = "addpatient"),
    path('adddoctor/', views.adddoctor, name = "adddoctor"),
    path('addreport/<int:id>/', views.addreport, name = "addreport"),
    path('deletepatient/<int:id>/', views.deletepatient, name = "deletepatient"),
    path('deletedoctor/<int:id>/', views.deletedoctor, name = "deletedoctor"),
    path('deletereport/<int:id>/', views.deletereport, name = "deletereport"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
    path('profile/', views.profile, name = "profile"),
    path('test/', views.testform, name = "test"),
    path('api/', include(router.urls)),
    path('classify/<int:id>/', views.get_prediction, name = "classify"),
] 