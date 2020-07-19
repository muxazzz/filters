from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import (ListView,
                                  DetailView, FormView)
from cars_libr.models import (Car, UserProfile)
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib import auth  
from django.http.response import HttpResponseRedirect  
from django.urls import reverse_lazy  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login, authenticate  
from cars_libr.forms import ProfileCreationForm  

class RegisterView(FormView):  
  
    form_class = UserCreationForm  
  
    def form_valid(self, form):  
        form.save()  
        username = form.cleaned_data.get('username')  
        raw_password = form.cleaned_data.get('password1')  
        login(self.request, authenticate(username=username, password=raw_password))  
        return super(RegisterView, self).form_valid(form)  
  
  
class CreateUserProfile(FormView):  
  
    form_class = ProfileCreationForm  
    template_name = 'profile-create.html'
    success_url = '127.0.0.1'
  
    def dispatch(self, request, *args, **kwargs):  
        if self.request.user.is_anonymous:  
            return HttpResponseRedirect('127.0.0.1')  
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)  
  
    def form_valid(self, form):  
        instance = form.save(commit=False)  
        instance.user = self.request.user  
        instance.save()  
        return super(CreateUserProfile, self).form_valid(form)

def index(request):  
    template_name = 'index.html'
    context = {}  
    if request.user.is_authenticated:  
        context['username'] = request.user.username  

    model = Car

    def get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()

        # search
        if get_params.get('q'):
      
            qs = qs.filter(Q(producer=get_params.get('q'))
            |Q(model=get_params.get('q')))
        return qs
    return render(request, 'index.html', context)


class CarListView(ListView):
    model = Car
    template = 'index.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()
        qs = Car.objects.all()
        # search
        if get_params.get('q'):
            gett = get_params.get('q').split(' ')
            for gets in gett:
                if gets.isdigit():
                    qs = qs.filter(Q(transmission=gets)
                    |Q(year=gets)
                    |Q(producer__in=gets)
                    |Q(model__in=gets)
                    |Q(color__in=gets))
                else:
                    qs = qs.filter(Q(producer__in=gett)
                    |Q(model__in=gett)
                    |Q(color__in=gett))
        return qs

class CarView(DetailView):

    model = Car
# Create your views here.

