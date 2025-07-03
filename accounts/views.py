from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login

from .forms import CustomLoginForm

class Signupview(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'


def custom_login(request):
    form = CustomLoginForm()
    if request.POST:
        form_obj = CustomLoginForm(data=request.POST)
        if form_obj.is_valid():

            username = form_obj.cleaned_data.get("username")
            password = form_obj.cleaned_data.get("password")

            password = request.POST.get('useri_pass')
            if username is not None and password:
                user = authenticate(
                    request, username=username, password=password
                )
                if user is not None:
                    login(request,user)
                    return redirect('home')
                else:
                    context = {'msg':'Nimaduram xatode'}
                    return render(request, 'customLogin.html', context)

        print(form_obj.errors)
        context = {'msg':'Welcome', "form":form, 'errors':form_obj.errors}
        return render(request, 'customLogin.html', context) 

    context = {'msg':'Welcome', "form":form}
    return render(request, 'customLogin.html', context)
