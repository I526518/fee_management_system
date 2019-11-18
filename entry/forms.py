from django import forms
from . import models

class DateInput(forms.DateInput):
    input_type='date'

class create_stud_pd(forms.ModelForm):
    class Meta:
        model = models.Stud_PD
        fields = ['Sname','USN','Gender','DOB','POB','S_Pno','S_Add','Batch']
        widgets = {'DOB':DateInput()}

class create_stud_admn(forms.ModelForm):
    class Meta:
        model = models.Stud_Admn
        fields = ['Adm_No','Course','Adm_Year','Sem','Branch','Adm_Type','Quota']