from django.shortcuts import render
from django.http import HttpResponse
from registration.models import Registration


# Create your views here.
def index(request):
    print(request.method)
    if request.method == 'POST':
        name = request.POST.get('fname')
        email = request.POST.get('email')
        m_no = request.POST.get('m_no')
        print(name, email, m_no)
        s = Registration(name=name, email=email, m_no=m_no)
        s.save()
        # sending data to html
    return render(request, 'index.html')


def display(request):
    x = Registration.objects.all()
    #x = Registration.objects.get(id=1)
    #output = "".join([(user.name + '<br>' + user.email + '<br>' + str(user.m_no) + '<br>') for user in x])
    context ={
        'obj': x

    }

    return render(request, 'display.html', context)




