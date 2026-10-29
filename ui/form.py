from django import forms
from .models import VmRequirements

class VmForm(forms.ModelForm):
    class Meta:
        model = VmRequirements
        fields = ['vm_name', 'ssh_key']