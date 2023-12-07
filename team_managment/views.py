from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .forms import MemberForm
from .models import Member

home_dir = '/'

class Home(ListView):
    model = Member
    context_object_name = 'members_list'
class Create(CreateView):
    model = Member
    form_class = MemberForm
    success_url = home_dir
class Details(UpdateView):
    model = Member
    form_class = MemberForm
    success_url = home_dir
class Delete(DeleteView):
    model = Member
    context_object_name = 'member'
    success_url = home_dir
