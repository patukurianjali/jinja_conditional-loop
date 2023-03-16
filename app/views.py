from django.shortcuts import render

# Create your views here.
def conditions (request):
    d={'a':17 , 'b':11,'c':123}
    return render(request,'conditions.html',d)
def loops(request):
    d={'name':'anjali'}
    return render(request,'loops.html',d)