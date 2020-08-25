from django import forms

from .models import NewOrder


class NewOrdertForm(forms.ModelForm):
    """Форма заявки на премию"""
    class Meta:
        model = NewOrder
        fields = '__all__'
