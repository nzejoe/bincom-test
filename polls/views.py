from django.shortcuts import render

from .models import PollingUnit, AnnouncedPuResults


def home(request):
    polling_units = PollingUnit.objects.all()

    context = {
        "polling_units": polling_units,
    }
    return render(request, "home.html", context)


def unit_results(request, unit_id):
    # get the informmation related to this polling unit
    polling_unit = PollingUnit.objects.get(uniqueid=unit_id)
    # get the election results for this polling unit
    unit_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unit_id).order_by("party_abbreviation")

    context = {
        "polling_unit": polling_unit,
        "unit_results": unit_results,
    }
    return render(request, "polls/unit_results.html", context)


def lga_results(request):
    return render(request, "polls/lga_results.html")
