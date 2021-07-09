from django.db.models import fields
from django.forms import ModelForm
from structure.models import ReadingArea, SetPositionMaster
from django import forms

class SetPositionMasterForm(ModelForm):
    ReadingAreaNo = forms.ModelChoiceField(queryset=ReadingArea.objects.order_by('ReadingAreaNo'))
    class Meta:
        model = SetPositionMaster
        fields = ['ReadingAreaNo','SetPositionCD','SetPositionNM','DeleteFlg']