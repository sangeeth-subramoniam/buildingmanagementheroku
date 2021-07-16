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
    ReadingAreaNo = models.IntegerField()
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


class SetPositionMaster(models.Model):
    ReadingAreaNo = models.ForeignKey(ReadingArea, on_delete=models.CASCADE)
    SetPositionCD = models.IntegerField()
    SetPositionNM = models.CharField(max_length=20)
    DeleteFlg =models.CharField(max_length=1 , blank = True)
    InsUserID =  models.CharField(max_length=20, null=True , default=None ,  blank = True)
    UpdUserID = models.CharField(max_length=20, null=True , default=None ,  blank = True)
    UpdDate = models.DateTimeField(auto_now=True,  blank = True)

    class Meta:
        unique_together = ['SetPositionCD','ReadingAreaNo']

    def __str__(self):
        return str(self.SetPositionNM)


class MeterMaster(models.Model):
    MeterID = models.IntegerField(unique=True)
    MeterNo = models.IntegerField()
    MeterKBN = models.IntegerField()
    ReadingAreaNo = models.ForeignKey(ReadingArea, on_delete=models.CASCADE)
    UseType = models.IntegerField()
    StoreNO = models.ForeignKey(StoreMaster,on_delete=models.CASCADE , related_name= 'storemaster')
    Magnification =  models.IntegerField()
    CommonType = models.IntegerField()
    ReadingStart =  models.IntegerField()
    SetPositionCD = models.ForeignKey(SetPositionMaster, on_delete=models.CASCADE)
    Remarks = models.CharField(max_length=200 , blank = True)
    DeleteFlg =models.CharField(max_length=1 , blank = True)
    InsUserID =  models.CharField(max_length=20, null=True , default=None ,  blank = True)
    UpdUserID = models.CharField(max_length=20, null=True , default=None ,  blank = True)
    UpdDate = models.DateTimeField(auto_now=True,  blank = True)

    def __str__(self):
        return str(self.MeterNo)