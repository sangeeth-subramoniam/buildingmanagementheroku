from django.db import models
from django.db.models.base import Model

# Create your models here.

class CodeMaster(models.Model):
    CodeType = models.CharField(max_length=4)
    CodeTypeNM = models.CharField(max_length=10)
    Code = models.CharField(max_length= 4)
    CodeNM = models.CharField(max_length= 20)
    Remarks = models.CharField(max_length=30 , blank = True)
    DeleteFlg = models.CharField(max_length=1 , blank = True)
    InsUserID = models.CharField(max_length = 20 , null=True , default=None , blank = True)
    UpdUserID = models.CharField(max_length=20 , null=True , default=None , blank = True)
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
    DeleteFlg = models.CharField(max_length=1 , blank = True)
    InsUserID =  models.CharField(max_length=20, null=True , default=None ,  blank = True)
    UpdUserID = models.CharField(max_length=20, null=True , default=None ,  blank = True)
    UpdDate = models.DateTimeField(auto_now=True,  blank = True)

    def __str__(self):
        return self.ReadingAreaNM

class StoreMaster(models.Model):
    StoreNO = models.IntegerField()
    ReadingAreaNo = models.ForeignKey(ReadingArea, on_delete=models.CASCADE)
    StoreType = models.IntegerField()
    StoreNM = models.CharField(max_length=40)
    ElectricBillingYMD = models.DateField(blank=True)
    GasBillingYMD = models.DateField(blank=True)
    WaterBillingYMD =  models.DateField(blank=True)
    DeleteFlg =models.CharField(max_length=1 , blank = True)
    InsUserID =  models.CharField(max_length=20, null=True , default=None ,  blank = True)
    UpdUserID = models.CharField(max_length=20, null=True , default=None ,  blank = True)
    UpdDate = models.DateTimeField(auto_now=True,  blank = True)

    class Meta:
        unique_together = ['StoreNO','ReadingAreaNo']

    def __str__(self):
        return str(self.StoreNM)