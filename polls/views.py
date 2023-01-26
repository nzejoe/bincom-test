from django.shortcuts import render, redirect
from django.db.models import Sum, Q

from .models import PollingUnit, AnnouncedPuResults, LGA, Party


def home(request):

    return render(request, "home.html")


def polling_units(request):
    polling_units = PollingUnit.objects.exclude(polling_unit_name__exact="")

    context = {
        "polling_units": polling_units,
    }
    return render(request, "polls/polling_units.html", context)


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

        # get all polling units IDs in the this lga
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
    polling_units = PollingUnit.objects.exclude(polling_unit_name__exact="")
    parties = Party.objects.all()

    # user location
    ip_address = request.META["REMOTE_ADDR"]

    if request.method == "POST":
        polling_unit = request.POST.get("polling_unit")
        agent_name = request.POST.get("agent_name")

        # get all parties result
        party_results = {
            "PDP": request.POST.get("PDP"),
            "DPP": request.POST.get("DPP"),
            "ACN": request.POST.get("ACN"),
            "PPA": request.POST.get("PPA"),
            "CDC": request.POST.get("CDC"),
            "JP": request.POST.get("JP"),
            "ANPP": request.POST.get("ANPP"),
            "LABOUR": request.POST.get("LABOUR"),
            "CPP": request.POST.get("CPP"),
        }

        for party, score in party_results.items():
            result = AnnouncedPuResults()
            result.polling_unit_uniqueid = polling_unit
            result.party_abbreviation = party
            result.party_score = score
            result.entered_by_user = agent_name
            result.user_ip_address = ip_address
            result.save()
        # redirect to polling uint results page
        return redirect("polls:unit_results", unit_id=polling_unit)

    context = {"polling_units": polling_units, "parties": parties}
    return render(request, "polls/add_results.html", context)
