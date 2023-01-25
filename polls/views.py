from functools import reduce

from django.shortcuts import render
from django.db.models import Sum, Q

from .models import PollingUnit, AnnouncedPuResults, LGA


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
    unit_results = AnnouncedPuResults.objects.filter(
        polling_unit_uniqueid=unit_id
    ).order_by("party_abbreviation")

    context = {
        "polling_unit": polling_unit,
        "unit_results": unit_results,
    }
    return render(request, "polls/unit_results.html", context)


def lga_results(request):
    lga_list = LGA.objects.all()

    lga = None
    pu_results = []
    lga_results = None

    if (
        request.method == "GET"
        and request.GET.get("lga")
        and request.GET.get("lga") != "all"
    ):
        lga_id = request.GET.get("lga")
        lga = LGA.objects.get(pk=lga_id)
        # print()
        # print(lga, lga_id)
        # print()
        # get the IDs of each polling unit
        polling_units = PollingUnit.objects.filter(lga_id=lga_id).values_list(
            "pk", flat=True
        )

        pu_results = [
            AnnouncedPuResults.objects.filter(polling_unit_uniqueid=id)
            for id in polling_units
        ]

        # if no polling unit result is fund
        if len(pu_results) == 0:
            lga_results = []
        else:
            lga_results = (
                pu_results[0]
                .values("party_abbreviation")
                .annotate(total_results=Sum("party_score"))
                .order_by("-total_results")
            )

    else:
        lga_results = (
            AnnouncedPuResults.objects.values("party_abbreviation")
            .annotate(total_results=Sum("party_score"))
            .order_by("-total_results")
        )

    context = {
        "lga": lga,
        "lga_list": lga_list,
        "lga_results": lga_results,
    }

    return render(request, "polls/lga_results.html", context)


def add_results(request):
    return render(request, "polls/add_results.html")
