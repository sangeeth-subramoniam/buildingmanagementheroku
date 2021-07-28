from django.db.models import fields
from django.forms import ModelForm
from structure.models import ReadingArea, Price
from django import forms

class SetPriceForm(ModelForm):
    ReadingAreaNo = forms.ModelChoiceField(queryset=ReadingArea.objects.order_by('ReadingAreaNo'))
    Total = forms.IntegerField()
    class Meta:
        model = Price
        fields = ['ReadingAreaNo','ProcessingYYYY','ProcessingMM','ElectricPrice','GasPrice','WaterPrice','ElectricAdjustment','GasAdjustment','WaterAdjustment' , 'Total']
    
    def __init__(self, *args, **kwargs):
        super(SetPriceForm, self).__init__(*args, **kwargs)

        if self.instance:
            self.fields['ReadingAreaNo'].disabled = True # still displays the field in the template
            self.fields['ProcessingYYYY'].disabled = True
            self.fields['ProcessingMM'].disabled = True
            self.fields['ElectricPrice'].disabled = True
            self.fields['GasPrice'].disabled = True
            self.fields['WaterPrice'].disabled = True
            
            # del self.fields['job'] # removes field from form and template
        #if self.instance and self.instance.level < 1:
            #self.fields['avatar'].disabled = True
    
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