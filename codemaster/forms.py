from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from structure.models import CodeMaster
from django import forms


class CodeMasterForm(ModelForm):
    class Meta:
        model = CodeMaster
        fields = ['CodeType','CodeTypeNM','Code','CodeNM','Remarks','DeleteFlg']
    
class CodeSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CodeSearchForm, self).__init__(*args, **kwargs)
        self.fields['CodeType'].required = False
        #self.fields['CodeTypeNM'].required = False
        #self.fields['Code'].required = False
        #self.fields['DeleteFlg'].required = False
        #self.fields['CodeType'].widget.attrs['cols'] = 100
        #self.fields['CodeType'].widget.attrs['rows'] = 200

    #tofieldname gives the value that needs to be passed on selection of the model choice field
    CodeType = forms.ModelChoiceField(queryset=CodeMaster.objects.all().order_by('CodeType') , to_field_name='id')

    class Meta:
        model = CodeMaster
        #fields = ['CodeType','CodeTypeNM','Code','DeleteFlg']
        fields = ['CodeType']