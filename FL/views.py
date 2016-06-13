from django.shortcuts import render

# Create your views here.
def bs_css(request):
    return render(request, 'bs_css.html')