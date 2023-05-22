from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app_django/index.html')

def hero(request):
    return render(request, 'app_django/main/app_django/hero.html')

def about(request):
    return render(request, 'app_django/main/app_django/about.html')

def main(request):
    return render(request, 'app_django/main/app_django/main.html')

# def why_us(request):
#     return render(request, 'app_django/main/app_django/why_us.html')

def menu(request):
    return render(request, 'app_django/main/app_django/menu.html')

def specials(request):
    return render(request, 'app_django/main/app_django/specials.html')

def events(request):
    return render(request, 'app_django/main/app_django/event.html')

def bookaTable(request):
    return render(request, 'app_django/main/app_django/bookaTable.html')

def testimonials(request):
    return render(request, 'app_django/main/app_django/testimonials.html')

def gallery(request):
    return render(request, 'app_django/main/app_django/gallery.html')

def chefs(request):
    return render(request, 'app_django/main/app_django/chef.html')

def contact(request):
    return render(request, 'app_django/main/app_django/contact.html')
