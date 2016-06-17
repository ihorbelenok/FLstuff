from django.shortcuts import render
import random

# Create your views here.
def bs_css(request):
    return render(request, 'bs_css.html')


def bs_components(request):
    return render(request, 'bs_components.html')


def bs_theme(request):
    return render(request, 'bs_theme.html')


def bs_just(request):
    return render(request, 'justified-nav.html')


def jq_functions(request):
    return render(request, 'jq_functions.html')


def jq_hw(request):
    return render(request, 'jq_hw.html')


def plugins(request):
    return render(request, 'jq_plugins.html')


def hw2_advanced(request):
    names = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta"]
    data = []
    for name in names:
        entryName = name
        numbers = [random.randint(0, 100) for i in range(50)]
        summ = sum(numbers)
        entry = {'name': entryName, 'numbers': numbers, 'summ': summ}
        data.append(entry)
    # print data
    return render(request, 'hw2_advanced.html', {'data': data})



def frontpage(request):
    return render(request, 'frontpage.html')
