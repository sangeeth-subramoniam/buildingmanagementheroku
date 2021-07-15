from django.db.models import fields
from django.forms import ModelForm
from structure.models import ReadingArea
from django import forms

class ReadingAreaForm(ModelForm):
    class Meta:
        model = ReadingArea
        fields = ['ReadingAreaNo','ReadingAreaNM','ElectricClaim','WaterClaim','GasClaim','DeleteFlg']

class AreaSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AreaSearchForm, self).__init__(*args, **kwargs)
        self.fields['DeleteFlg'].required = False
        #self.fields['CodeTypeNM'].required = False
        #self.fields['Code'].required = False
        #self.fields['DeleteFlg'].required = False
        #self.fields['CodeType'].widget.attrs['cols'] = 100
        #self.fields['CodeType'].widget.attrs['rows'] = 200

    #tofieldname gives the value that needs to be passed on selection of the model choice field
    #CodeType = forms.ModelChoiceField(queryset=CodeMaster.objects.all().order_by('CodeType') , to_field_name='id')
    DeleteFlg = forms.BooleanField()

    class Meta:
        model = ReadingArea
        #fields = ['CodeType','CodeTypeNM','Code','DeleteFlg']
        fields = ['DeleteFlg']