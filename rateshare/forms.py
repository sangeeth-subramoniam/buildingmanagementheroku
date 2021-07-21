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
            
            #self.fields['StoreNo'].queryset = self.instance.ReadingAreaNo.StoreNo_set
            #self.fields['StoreNo'].queryset = StoreMaster.objects.filter(self.instance.ReadingAreaNo)
            #self.fields['StoreNo'].queryset = StoreMaster.objects.filter(ReadingArea.objects.get(self.instance.ReadingAreaNo))
            #self.fields['StoreNo'] = ['aaa' , 'bbb' , 'ccc']
            self.fields['StoreNO'].queryset = StoreMaster.objects.filter(ReadingAreaNo__ReadingAreaNo = self.instance.ReadingAreaNo.ReadingAreaNo)
            self.fields['MeterID'].queryset = StoreMaster.objects.filter(ReadingAreaNo__ReadingAreaNo = self.instance.ReadingAreaNo.ReadingAreaNo , MeterKBN = self.instance.MeterKBN)



class RateSharingUpdateForm(ModelForm):
    class Meta:
        model = RateShare
        fields = ['Rate','Remarks','DeleteFlg']

    

class RateSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RateSearchForm, self).__init__(*args, **kwargs)

        self.fields['ProcessingYYYY'].required = False
        self.fields['ProcessingMM'].required = False

        self.fields['ReadingAreaNo2'].required = False
        self.fields['ReadingAreaNo2'].label = 'ReadingAreaNo'

        self.fields['MeterKBN2'].required = False
        self.fields['MeterKBN2'].label = 'MeterKBN'

        self.fields['MeterID2'].required = False
        self.fields['MeterID2'].label = 'MeterID'
        
        self.fields['DeleteFlg'].required = False
        #self.fields['CodeType'].widget.attrs['cols'] = 100
        #self.fields['CodeType'].widget.attrs['rows'] = 200

    #tofieldname gives the value that needs to be passed on selection of the model choice field
    ReadingAreaNo2 = forms.ModelChoiceField(queryset=ReadingArea.objects.all().order_by('ReadingAreaNo') , to_field_name='id')
    MeterKBN2 = forms.ModelChoiceField(queryset=CodeMaster.objects.filter(CodeType='0010').order_by('Code') , to_field_name='Code')
    MeterID2 =  forms.ModelChoiceField(queryset=RateShare.objects.none())
    DeleteFlg = forms.BooleanField()

    ProcessingYYYY = forms.CharField(max_length=4)
    ProcessingMM = forms.CharField(max_length=2)

    class Meta:
        model = RateShare
        #fields = ['CodeType','CodeTypeNM','Code','DeleteFlg']
        fields = ['ProcessingYYYY','ProcessingMM','ReadingAreaNo2','MeterKBN2','MeterID2','DeleteFlg']            