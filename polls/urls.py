from django.urls import path

from . import views


app_name = "polls"

urlpatterns = [
    path("", views.home, name="home"),
    path("polling_unit_results/<int:unit_id>/", views.unit_results, name="unit_results"),
]
