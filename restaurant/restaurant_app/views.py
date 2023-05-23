from django.shortcuts import render

def menu(request):
    # написать
    return render(request, 'restaurant_app/menu.html')
