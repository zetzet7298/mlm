from django import forms
from . import models

class ClientTypeForm(forms.ModelForm):
    class Meta:
        model = models.ClientType
        # fields = ['name', 'desc']
        fields = "__all__"
