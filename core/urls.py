from django.urls import path

from .views import IndexView, doctor_name_ajax

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('/doctor_name/', doctor_name_ajax, name="doctor_name_ajax" ),
]