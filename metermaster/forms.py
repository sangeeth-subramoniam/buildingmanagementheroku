from django.db.models import fields
from django.forms import ModelForm
from structure.models import MeterMaster,ReadingArea, StoreMaster

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
            self.fields['StoreNo'].queryset = self.instance.ReadingAreaNo.StoreNO_set.order_by('StoreNM')