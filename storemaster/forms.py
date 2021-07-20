from django.db.models import fields
from django.forms import ModelForm
from structure.models import ReadingArea, StoreMaster
from django import forms

class StoreMasterForm(ModelForm):
    ReadingAreaNo = forms.ModelChoiceField(queryset=ReadingArea.objects.order_by('ReadingAreaNo'))
    class Meta:
        model = StoreMaster
        fields = ['StoreNO','ReadingAreaNo','StoreType','StoreNM','ElectricBillingYMD','GasBillingYMD','WaterBillingYMD','DeleteFlg']

class StoreSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StoreSearchForm, self).__init__(*args, **kwargs)
        self.fields['ReadingAreaNo'].required = False
        #self.fields['CodeTypeNM'].required = False
        #self.fields['Code'].required = False
        self.fields['DeleteFlg'].required = False
        #self.fields['CodeType'].widget.attrs['cols'] = 100
        #self.fields['CodeType'].widget.attrs['rows'] = 200

    #tofieldname gives the value that needs to be passed on selection of the model choice field
    ReadingAreaNo = forms.ModelChoiceField(queryset=ReadingArea.objects.all().order_by('ReadingAreaNo') , to_field_name='id')
    DeleteFlg = forms.BooleanField()

    class Meta:
        model = StoreMaster
        #fields = ['CodeType','CodeTypeNM','Code','DeleteFlg']
        fields = ['ReadingAreaNo','DeleteFlg']
