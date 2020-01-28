from django import forms
from .models import Chair


class ProductForm(forms.ModelForm):
    class Meta:
        model = Chair
        fields = ('type', 'price', 'status', 'issues')



