from django import forms
from .models import TodoModel

class UpdateForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['value']
        widgets = {'value': forms.TextInput(attrs={'class':'txt'})}
