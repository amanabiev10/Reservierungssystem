from django.shortcuts import render


def index(request):
    tables = range(1, 11)
    context = {
        'tables': tables
    }
    return render(request, 'home/index.html', context)