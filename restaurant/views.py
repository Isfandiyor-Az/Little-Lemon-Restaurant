from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Menu
from .forms import BookingForm
# Create your views here.

def handler404(request, exception):
    return HttpResponse("<h1>Don't worry, 404 error occurred!</h1> <p>If you really want to see detailed url, then set DEBUG=True, to view every ulrs where you can reach.</p>")

def home(request):
    return render(request, 'index.html', {})

def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request,'about.html',about_content)


def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book')
    return render(request,'book.html',{'form':form})

def menu(request):
    menu_data = Menu.objects.all()
    menu_content = {'menu':menu_data}
    return render(request, 'menu.html', menu_content)

def display_menu_items(request,pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)

    else:
        menu_item = ""
    
    return render(request,'menu_item.html',{"menu_item":menu_item})


