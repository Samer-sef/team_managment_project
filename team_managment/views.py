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
            form = MemberForm(instance=Member.objects.get(pk=id))
        return render(request, 'details_page.html', {'form': form})
    else:
        if id == 0:
            form = MemberForm(request.POST)
        else:
            form = MemberForm(request.POST, instance=Member.objects.get(pk=id))
        if form.is_valid():
            form.save()
        return redirect('/')
    
def delete(request, id=0):
    Member.objects.get(pk=id).delete()
    return redirect('/')


