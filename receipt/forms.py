from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from structure.models import CodeMaster
from django import forms

class myForm(forms.Form):
    # ...
    date = forms.DateField(
        required=False,
        widget=MonthYearWidget(years=xrange(2004,2010))
    )