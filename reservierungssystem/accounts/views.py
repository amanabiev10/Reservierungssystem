from django.shortcuts import render, HttpResponseRedirect, HttpResponse


def index(request):
    return HttpResponse('Hallo Welt')