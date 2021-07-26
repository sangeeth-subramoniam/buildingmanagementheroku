from django.db.models import fields
from django.forms import ModelForm
from structure.models import ReadingArea, Price
from django import forms

class SetPriceForm(ModelForm):
    ReadingAreaNo = forms.ModelChoiceField(queryset=ReadingArea.objects.order_by('ReadingAreaNo'))
    class Meta:
        model = Price
        fields = ['ReadingAreaNo','ProcessingYYYY','ProcessingMM','ElectricPrice','GasPrice','WaterPrice']

class SetPriceSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SetPriceSearchForm, self).__init__(*args, **kwargs)
        self.fields['ProcessingYYYY'].required = False
        #self.fields['CodeTypeNM'].required = False
        #self.fields['Code'].required = False
        self.fields['ProcessingMM'].required = False
        #self.fields['CodeType'].widget.attrs['cols'] = 100
        #self.fields['CodeType'].widget.attrs['rows'] = 200

    #tofieldname gives the value that needs to be passed on selection of the model choice field

    class Meta:
        model = Price
        #fields = ['CodeType','CodeTypeNM','Code','DeleteFlg']
        fields = ['ProcessingYYYY','ProcessingMM']