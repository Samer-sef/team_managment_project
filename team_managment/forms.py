from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    mobile = forms.IntegerField()
    email = forms.EmailField()
    class Meta:
        model = Member
        # Keep this oder in the UI
        fields = ['first_name', 'last_name', 'email', 'mobile', 'role']
        widgets = {
               'role': forms.RadioSelect()
           }