from django.shortcuts import render

# Create your views here.
def bs_css(request):
    return render(request, 'bs_css.html')


def bs_components(request):
    return render(request, 'bs_components.html')


def bs_theme(request):
    return render(request, 'bs_theme.html')


def bs_just(request):
    return render(request, 'justified-nav.html')


def frontpage(request):
    return render(request, 'frontpage.html')
