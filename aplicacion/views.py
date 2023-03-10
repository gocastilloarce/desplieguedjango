from django.shortcuts import render

# Create your views here.
def ee(request):
    return render(request,"aplicacion/esto.html", {})