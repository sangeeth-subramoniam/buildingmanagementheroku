from django.db.models import fields
from django.forms import ModelForm
from structure.models import *
from django import forms

class RateSharingForm(ModelForm):
    ReadingAreaNo = forms.ModelChoiceField(queryset=ReadingArea.objects.all())
    MeterKBN = forms.ModelChoiceField(queryset=CodeMaster.objects.all().filter(CodeType = '0010'))
    class Meta:
        model = RateShare
        fields = ['ReadingAreaNo','MeterKBN','MeterID','StoreNO','ProcessingYYYY','ProcessingMM','Rate','Remarks','DeleteFlg']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['StoreNO'].queryset = ReadingArea.objects.none()
        self.fields['MeterID'].queryset = MeterMaster.objects.none()

        if 'ReadingAreaNo' in self.data:
            try:
                ReadingAreaNo_id = int(self.data.get('ReadingAreaNo'))
                MeterKBN= int(self.data.get('MeterKBN'))
                self.fields['StoreNO'].queryset = StoreMaster.objects.filter(ReadingAreaNo_id=ReadingAreaNo_id).order_by('StoreNM')
                self.fields['MeterID'].queryset = MeterMaster.objects.filter(ReadingAreaNo_id=ReadingAreaNo_id , MeterKBN = MeterKBN).order_by('MeterID')
                
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
            self.fields['MeterID'].queryset = StoreMaster.objects.filter(ReadingAreaNo__ReadingAreaNo = self.instance.ReadingAreaNo.ReadingAreaNo , MeterKBN = self.instance.MeterKBN)



            