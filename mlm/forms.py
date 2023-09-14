from django import forms
from core import models

class MultiLevelForm(forms.ModelForm):
    class Meta:
        model = models.MultiLevel
        # fields = ['name', 'email', 'password1', 'password2']
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(MultiLevelForm, self).__init__(*args, **kwargs)
        self.fields['user_defined_code']=forms.ModelChoiceField(queryset=UserDefinedCode.objects.filter(owner=user))
