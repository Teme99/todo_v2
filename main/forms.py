from django import forms
from .models import Plans

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plans
        fields = ['name', 'detail']