from django.urls import path

from .views import IndexView, SearchView


app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('search/', SearchView.as_view(), name="search"),
]