from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'library/home.html')

    
def vista1(request):
    return render(request, 'library/vista1.html')

def vista2(request):
    return render(request, 'library/vista2.html')

def vista3(request):
    return render(request, 'library/vista3.html')

def vista4(request):
    return render(request, 'library/vista4.html')

