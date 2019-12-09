from django.shortcuts import render

from homework.models import HW


def db(request):
    homeworks = HW.objects.all()
    return render(request, "db.html", {'homeworks': homeworks})
