from django.urls import path

from .views import IndexView, doctor_name_ajax, SearchView


app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('doctor_name/<int:id>/', doctor_name_ajax, name="doctor_name_ajax" ),
    path('search/', SearchView.as_view(), name="search"),
]