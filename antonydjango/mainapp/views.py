from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.

def index(request):
    data = {
        'title': 'New Main page here ',
        'values': ['Some','Hello',12345 ],
        'obj': {
            'car': ' BMW',
            'age': 18,
            'hobby': 'MYM'
        }
    }
    return render(request, 'mainapp/index.html', data)


def about(request):
    return render(request, 'mainapp/about.html')





