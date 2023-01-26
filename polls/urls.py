from django.urls import path

from . import views


app_name = "polls"

urlpatterns = [
    path("", views.home, name="home"),
    path("polling_units/", views.polling_units, name="polling_units"),
    path("polling_units/<int:unit_id>/", views.unit_results, name="unit_results"),
    path("lga_results/", views.lga_results, name="lga_results"),
    path("add_results/", views.add_results, name="add_results"),
]
