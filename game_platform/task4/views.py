from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'fourth_task/platform_main.html')

def contacts(request):
    return render(request, 'fourth_task/contacts.html')