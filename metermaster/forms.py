from django.db.models import fields
from django.forms import ModelForm
from structure.models import MeterMaster

class MeterMasterForm(ModelForm):
    class Meta:
        model = MeterMaster
        fields = ['MeterID','MeterNo','MeterKBN','ReadingAreaNo','UseType','StoreNO','Magnification','CommonType','ReadingStart','SetPositionCD','Remarks','DeleteFlg']