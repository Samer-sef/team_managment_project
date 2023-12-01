from django import forms
from .models import Member

class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        # Keep this oder in the UI
        fields = ['first_name', 'last_name', 'email', 'mobile', 'role']
        widgets = {
               'role': forms.RadioSelect()
           }