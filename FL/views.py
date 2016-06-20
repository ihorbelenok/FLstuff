from django.shortcuts import render
from django.http import HttpResponse
import json
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
    total = 0
    for name in names:
        entryName = name
        numbers = [random.randint(0, 100) for i in range(20)]
        summ = sum(numbers)
        total += summ
        entry = {'name': entryName, 'numbers': numbers, 'summ': summ}
        data.append(entry)
    # print data
    return render(request, 'hw2_advanced.html', {'data': data, 'total': total})

def hw2_json(request):
    data = []
    for i in range(1000):
        entry={}
        entry['name'] = 'Name'+str(i)
        entry['marks'] = [random.randint(1, 12) for i in range(6)]
        data.append(entry)

    # print data
    return HttpResponse('{"data":'+json.dumps(data)+'}')

def hw2_table_json(request):
    return render(request, 'hw2_advanced_json.html')

def hw3(request):
    return render(request, 'hw3/landing.html')




def frontpage(request):
    return render(request, 'frontpage.html')
