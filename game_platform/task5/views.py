from django.shortcuts import render
from .forms import Reg_form
from django.http import HttpResponse
from .models import Buyer
from .models import Game


def search(usname):
    userses = Buyer.objects.filter(username = usname)
    if userses.exists():
        return True
    else:
        False



def index(request):
    if request.method == 'POST':
        form = Reg_form(request.POST)
        condition = False
        age_no = False
        user_no = False
        succses = False
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            
            if password != repeat_password:
                condition = True
                context = {
                    'condition' : condition
                }
                # Возвращаем ответ с текстом в виде HTML, если условие истинно
                return render(request, 'fifth_task/registration_page.html', context)
            elif int(age) < 18:
                age_no = True
                context = {
                    'age_no' : age_no
                }
                # Возвращаем ответ с текстом в виде HTML, если условие истинно
                return render(request, 'fifth_task/registration_page.html', context)
            elif search(username):
                user_no = True
                context = {
                    'user_no' : user_no
                }
                # Возвращаем ответ с текстом в виде HTML, если условие истинно
                return render(request, 'fifth_task/registration_page.html', context)
            else:
                succses = True
                user = Buyer.objects.create(username=username, password= password, age = age)
                context = {
                    'succses' : succses
                }
                return render(request, 'fifth_task/registration_page.html', context)
                


                

                

    else:
        form = Reg_form()
    return render(request, 'fifth_task/registration_page.html', {'form': form})
# Create your views here.
def games(request):
    Games = Game.objects.all()
    context = {
        'Games': Games,
    }
    return render(request,'fourth_task/buy.html', context)