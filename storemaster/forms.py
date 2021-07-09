from django.db.models import fields
from django.forms import ModelForm
from structure.models import ReadingArea, StoreMaster
from django import forms

class StoreMasterForm(ModelForm):
    ReadingAreaNo = forms.ModelChoiceField(queryset=ReadingArea.objects.order_by('ReadingAreaNo'))
    class Meta:
        model = StoreMaster
        fields = ['StoreNO','ReadingAreaNo','StoreType','StoreNM','ElectricBillingYMD','GasBillingYMD','WaterBillingYMD','DeleteFlg']