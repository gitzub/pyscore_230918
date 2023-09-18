from django.shortcuts import render
from .models import ViewGame
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.http import HttpResponseBadRequest, JsonResponse


def pyhome(request):
    return render(request, "pyhome.html")


def gamelist(request):
    return render(request, "aaatest.html")


def gamelist_data(request):
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        start = request.GET.get("start")
        end = request.GET.get("end")

        try:
            start_date = datetime.strptime(start, "%Y-%m").date()
        except Exception:
            start_date = date.today().replace(day=1)

        try:
            end_date = datetime.strptime(end, "%Y-%m").date()
        except Exception:
            end_date = date.today()

        if start_date > end_date:
            end_date, start_date = start_date, end_date

        end_date += relativedelta(day=31)

        return JsonResponse(
            {
                "data": list(
                    ViewGame.objects.filter(
                        gamedate__range=[start_date, end_date]
                    ).values()
                )
            }
        )
    else:
        return HttpResponseBadRequest("Invalid request")
