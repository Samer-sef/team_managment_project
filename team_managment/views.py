from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member


def home(request):
    context = {'members_list': Member.objects.all()}
    return render(request, 'list_page.html', context)

def details(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MemberForm()
        else:
            member = Member.objects.get(pk=id)
            form = MemberForm(instance=member)
        return render(request, 'details_page.html', {'form': form})
    else:
        if id == 0:
            form = MemberForm(request.POST)
        else:
            member = Member.objects.get(pk=id)
            form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
        return redirect('/')


