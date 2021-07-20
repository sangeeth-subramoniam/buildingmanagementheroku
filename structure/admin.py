from typing import Set
from django.contrib import admin
from .models import ReadingArea,CodeMaster,StoreMaster,SetPositionMaster,MeterMaster,RateShare
# Register your models here.

admin.site.register(ReadingArea)
admin.site.register(CodeMaster)
admin.site.register(StoreMaster)
admin.site.register(SetPositionMaster)
admin.site.register(MeterMaster)
admin.site.register(RateShare)