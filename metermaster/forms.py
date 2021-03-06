from types import CodeType
from django.db.models import fields
from django.forms import ModelForm
from structure.models import *
from django import forms

class MeterMasterForm(ModelForm):
    class Meta:
        model = MeterMaster
        fields = ['MeterID','MeterNo','MeterKBN','ReadingAreaNo','UseType','StoreNO','Magnification','CommonType','ReadingStart','SetPositionCD','Remarks','DeleteFlg']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['StoreNO'].queryset = ReadingArea.objects.none()

        if 'ReadingAreaNo' in self.data:
            try:
                ReadingAreaNo_id = int(self.data.get('ReadingAreaNo'))
                self.fields['StoreNO'].queryset = StoreMaster.objects.filter(ReadingAreaNo_id=ReadingAreaNo_id).order_by('StoreNM')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            print('aaaaaa' , self.instance.ReadingAreaNo.id)
            print('bbbbb' , StoreMaster.objects.filter(ReadingAreaNo__ReadingAreaNo = self.instance.ReadingAreaNo.ReadingAreaNo))
            #self.fields['StoreNo'].queryset = self.instance.ReadingAreaNo.StoreNo_set
            #self.fields['StoreNo'].queryset = StoreMaster.objects.filter(self.instance.ReadingAreaNo)
            #self.fields['StoreNo'].queryset = StoreMaster.objects.filter(ReadingArea.objects.get(self.instance.ReadingAreaNo))
            #self.fields['StoreNo'] = ['aaa' , 'bbb' , 'ccc']
            self.fields['StoreNO'].queryset = StoreMaster.objects.filter(ReadingAreaNo__ReadingAreaNo = self.instance.ReadingAreaNo.ReadingAreaNo)


class MeterSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MeterSearchForm, self).__init__(*args, **kwargs)
        self.fields['ReadingAreaNo2'].required = False
        self.fields['ReadingAreaNo2'].label = 'ReadingAreaNo'


        self.fields['MeterKBN'].required = False
        self.fields['UseType'].required = False
        self.fields['DeleteFlg'].required = False
        #self.fields['CodeType'].widget.attrs['cols'] = 100
        #self.fields['CodeType'].widget.attrs['rows'] = 200

    #tofieldname gives the value that needs to be passed on selection of the model choice field
    ReadingAreaNo2 = forms.ModelChoiceField(queryset=ReadingArea.objects.all().order_by('ReadingAreaNo') , to_field_name='id')
    MeterKBN = forms.ModelChoiceField(queryset=CodeMaster.objects.filter(CodeType='0010').order_by('Code') , to_field_name='Code')
    UseType = forms.IntegerField()
    DeleteFlg = forms.BooleanField()

    class Meta:
        model = StoreMaster
        #fields = ['CodeType','CodeTypeNM','Code','DeleteFlg']
        fields = ['ReadingAreaNo2','MeterKBN','UseType','DeleteFlg']
