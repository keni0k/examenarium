from django.shortcuts import render


def db(request):
    return render(request, "db.html", {})