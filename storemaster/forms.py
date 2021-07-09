from django.db.models import fields
from django.forms import ModelForm
from structure.models import StoreMaster

class StoreMasterForm(ModelForm):
    class Meta:
        model = StoreMaster
        fields = ['StoreNO','ReadingAreaNo','StoreType','StoreNM','ElectricBillingYMD','GasBillingYMD','WaterBillingYMD','DeleteFlg']