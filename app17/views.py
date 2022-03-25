from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':50,'b':50,'c':'98'}
    return render(request,'conditions.html',d)

def loops(request):
    d={'name':'manoj'}
    return render(request,'loops.html',d)