from django.db import models
from django.db.models.base import Model

# Create your models here.

class CodeMaster(models.Model):
    CodeType = models.CharField(max_length=4)
    CodeTypeNM = models.CharField(max_length=10)
    Code = models.CharField(max_length= 4)
    CodeNM = models.CharField(max_length= 20)
    Remarks = models.CharField(max_length=30)
    DeleteFlg = models.CharField(max_length=1)
    InsDate = models.DateTimeField(auto_created=True)
    InsUserID = models.CharField(max_length = 20)
    UpdUserID = models.CharField(max_length=20)
    UpdDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['CodeType','Code']

    def __str__(self):
        return self.CodeNM
    



class ReadingArea(models.Model):
    ReadingAreaNo = models.IntegerField(primary_key=True)
    ReadingAreaNM = models.CharField(max_length=20)
    ElectricClaim = models.IntegerField()
    WaterClaim = models.IntegerField()
    GasClaim = models.IntegerField()
    DeleteFlg = models.CharField(max_length=1)
    InsUserID =  models.CharField(max_length=20)
    UpdUserID = models.CharField(max_length=20)
    UpdDate = models.DateTimeField()

    def __str__(self):
        return self.ReadingAreaNM

    