from django.db.models import fields
from django.forms import ModelForm
from structure.models import CodeMaster

class CodeMasterForm(ModelForm):
    class Meta:
        model = CodeMaster
        fields = ['CodeType','CodeTypeNM','Code','CodeNM','Remarks','DeleteFlg']