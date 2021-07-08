from django.db.models import fields
from django.forms import ModelForm
from structure.models import ReadingArea

class ReadingAreaForm(ModelForm):
    class Meta:
        model = ReadingArea
        fields = ['ReadingAreaNo','ReadingAreaNM','ElectricClaim','WaterClaim','GasClaim','DeleteFlg']