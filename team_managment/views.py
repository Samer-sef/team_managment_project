from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member


def home(request):
    context = {'members_list': Member.objects.all()}
    return render(request, 'list_page.html', context)

def details(request):
    if request.method == "GET":
        form = MemberForm()
        return render(request, 'details_page.html', {'form': form})
    else:
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


