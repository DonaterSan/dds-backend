from django.shortcuts import render


def index(request):
    return render(request, "cashflow/index.html")


def references(request):
    return render(request, "cashflow/references.html")
