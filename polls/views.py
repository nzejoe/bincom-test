from django.shortcuts import render

from .models import PollingUnit


def home(request):
    polling_units = PollingUnit.objects.all()
    print()
    print(polling_units)
    print()
    context = {
        "polling_units": polling_units,
    }
    return render(request, "home.html", context)
