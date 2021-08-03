from typing import Union
from django.db.models.expressions import OuterRef
import receipt
from django.shortcuts import render,redirect
from structure.models import Price,MeterMaster,RateShare,MeterReading, CodeMaster
from django.core.paginator import Paginator
from django.db import models
from django.db.models import Q , Subquery, F
from decimal import Decimal

# Create your views here.
def home(request):

    class receipt :
        def __init__(self,MeterID,ReadingAreaNo,ReadingYYYY,ProcessingMM,MeterKBN, price_per_unit , rate_share , total_estimate):
            self.MeterID = MeterID
            self.ReadingAreaNo = ReadingAreaNo
            self.ReadingYYYY = ReadingYYYY
            self.ProcessingMM = ProcessingMM
            self.MeterKBN = MeterKBN
            self.price_per_unit = price_per_unit
            self.rate_share = round(rate_share,2)
            self.total_estimate = round(total_estimate,2)

        def __str__(self):
            return str(str(self.MeterID) + str(self.ReadingYYYY) + str(self.ProcessingMM))

    def val_kbn(a):
        code_kbn = CodeMaster.objects.filter(CodeType = "0010" , Code = a)
        return(code_kbn[0].CodeNM)


    #POST


    
    if request.method == 'POST':

        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        print('year is ', year)

        meterread_data = MeterReading.objects.all().order_by('ReadingYYYY','ProcessingMM','MeterID__MeterKBN')
        price_data = Price.objects.all()

        print('data is ', meterread_data)
        print('data2 is ', price_data)

        
        ls = []

        for m in  range(0,meterread_data.count()):
            print(m)
                        
            #er is changed to true if there is no amount per unit set and amt is for calculating total estimate
            er = False
            share = False
            shareval = 0
            amt = 0
            
            
            print('Meter ID : ',meterread_data[m].MeterID)
            print('ReadArea : ',meterread_data[m].MeterID.ReadingAreaNo)
            print('ReadingYear : ',meterread_data[m].ReadingYYYY)
            print('ReadingMonth : ',meterread_data[m].ProcessingMM)
            
            
            val = price_data.filter(ProcessingYYYY = meterread_data[m].ReadingYYYY , ProcessingMM = meterread_data[m].ProcessingMM , ReadingAreaNo = meterread_data[m].MeterID.ReadingAreaNo)
            
            kbntype = val_kbn(meterread_data[m].MeterID.MeterKBN)
            print('The Meter Division Type is : ' , val_kbn(meterread_data[m].MeterID.MeterKBN))
            
            
            def novalset():
                er = True
                print('There is no value set... Please contact admin')

            
            if(meterread_data[m].MeterID.MeterKBN == 1 ):
                if(val.count() == 0):
                    novalset()
                else:
                    amt = meterread_data[m].Using * val[0].ElectricPrice
                    print('amt is ', amt )
                    ppu = val[0].ElectricPrice
                    print('Price per unit of Electric Meter Set is ' , val[0].ElectricPrice)
            
            
            if(meterread_data[m].MeterID.MeterKBN == 2 ):
                if(val.count() == 0):
                    novalset()
                else:
                    amt = meterread_data[m].Using * val[0].GasPrice
                    print('amt is ', amt )
                    ppu = val[0].GasPrice
                    print('Price per unit of Gas Meter Set is ' , val[0].GasPrice)
            
            
            if(meterread_data[m].MeterID.MeterKBN == 3 ):
                if(val.count() == 0):
                    novalset()
                else:
                    amt = meterread_data[m].Using * val[0].WaterPrice
                    print('amt is ', amt )
                    ppu = val[0].WaterPrice
                    print('Price per unit of Water Meter Set is ' , val[0].WaterPrice)

            
            rs = RateShare.objects.all().filter(MeterID = meterread_data[m].MeterID , StoreNO = meterread_data[m].MeterID.StoreNO , ProcessingYYYY = meterread_data[m].ReadingYYYY , ProcessingMM =  meterread_data[m].ProcessingMM )
            
            if(rs.count() != 0):
                share = True
                if rs[0].Rate > 0:
                    shareval = (rs[0].Rate * Decimal(0.01))
                else : 
                    shareval = 1

                print('rate sharing is ', rs[0].Rate ,' - ' , rs[0].Remarks)
            else:
                print('This Meter is not Shared')

            if er:
                print('Oops ! There was an error during the estimation. Please contact the admin' )
            else:
                if share:
                    tot_estimate = amt * shareval
                    print('Amount to pay : ', round(tot_estimate, 2))
                else:
                    tot_estimate = amt
                    print('Amount to pay : ', round(amt,2))


            print('--------------------------------------------------------------------------------------')
            
            r2 = receipt(meterread_data[m].MeterID,meterread_data[m].MeterID.ReadingAreaNo,meterread_data[m].ReadingYYYY,meterread_data[m].ProcessingMM,kbntype,ppu,shareval,tot_estimate)
            
            if(year == int(meterread_data[m].ReadingYYYY) and month == int(meterread_data[m].ProcessingMM)) :
                ls.append(r2)
            
            context = {

                'values' : ls        
            }

        print('list set is sdfsdf' , ls)
        return render(request,'receipt/home.html' , context)





    #GET



    #receipt = Price.objects.filter(Q(ElectricPrice__gte=151)).order_by("-ElectricPrice")[:5]

    meterread_data = MeterReading.objects.all().order_by('ReadingYYYY','ProcessingMM','MeterID__MeterKBN')
    price_data = Price.objects.all()

    print('data is ', meterread_data)
    print('data2 is ', price_data)

    
    ls = []
    for m in  range(0,meterread_data.count()):

        class receipt :
            def __init__(self,MeterID,ReadingAreaNo,ReadingYYYY,ProcessingMM,MeterKBN, price_per_unit , rate_share , total_estimate):
                self.MeterID = MeterID
                self.ReadingAreaNo = ReadingAreaNo
                self.ReadingYYYY = ReadingYYYY
                self.ProcessingMM = ProcessingMM
                self.MeterKBN = MeterKBN
                self.price_per_unit = price_per_unit
                self.rate_share = round(rate_share,2)
                self.total_estimate = round(total_estimate,2)

            def __str__(self):
                return str(str(self.MeterID) + str(self.ReadingYYYY) + str(self.ProcessingMM))

        
        #er is changed to true if there is no amount per unit set and amt is for calculating total estimate
        er = False
        share = False
        shareval = 0
        amt = 0
        
        
        print('Meter ID : ',meterread_data[m].MeterID)
        print('ReadArea : ',meterread_data[m].MeterID.ReadingAreaNo)
        print('ReadingYear : ',meterread_data[m].ReadingYYYY)
        print('ReadingMonth : ',meterread_data[m].ProcessingMM)
        
        
        val = price_data.filter(ProcessingYYYY = meterread_data[m].ReadingYYYY , ProcessingMM = meterread_data[m].ProcessingMM , ReadingAreaNo = meterread_data[m].MeterID.ReadingAreaNo)
        
        kbntype = val_kbn(meterread_data[m].MeterID.MeterKBN)
        print('The Meter Division Type is : ' , val_kbn(meterread_data[m].MeterID.MeterKBN))
        
        
        def novalset():
            er = True
            print('There is no value set... Please contact admin')

        
        if(meterread_data[m].MeterID.MeterKBN == 1 ):
            if(val.count() == 0):
                novalset()
            else:
                amt = meterread_data[m].Using * val[0].ElectricPrice
                print('amt is ', amt )
                ppu = val[0].ElectricPrice
                print('Price per unit of Electric Meter Set is ' , val[0].ElectricPrice)
        
        
        if(meterread_data[m].MeterID.MeterKBN == 2 ):
            if(val.count() == 0):
                novalset()
            else:
                amt = meterread_data[m].Using * val[0].GasPrice
                print('amt is ', amt )
                ppu = val[0].GasPrice
                print('Price per unit of Gas Meter Set is ' , val[0].GasPrice)
        
        
        if(meterread_data[m].MeterID.MeterKBN == 3 ):
            if(val.count() == 0):
                novalset()
            else:
                amt = meterread_data[m].Using * val[0].WaterPrice
                print('amt is ', amt )
                ppu = val[0].WaterPrice
                print('Price per unit of Water Meter Set is ' , val[0].WaterPrice)

        
        rs = RateShare.objects.all().filter(MeterID = meterread_data[m].MeterID , StoreNO = meterread_data[m].MeterID.StoreNO , ProcessingYYYY = meterread_data[m].ReadingYYYY , ProcessingMM =  meterread_data[m].ProcessingMM )
        
        if(rs.count() != 0):
            share = True
            if rs[0].Rate > 0:
                shareval = (rs[0].Rate * Decimal(0.01))
            else : 
                shareval = 1

            print('rate sharing is ', rs[0].Rate ,' - ' , rs[0].Remarks)
        else:
            print('This Meter is not Shared')

        if er:
            print('Oops ! There was an error during the estimation. Please contact the admin' )
        else:
            if share:
                tot_estimate = amt * shareval
                print('Amount to pay : ', round(tot_estimate, 2))
            else:
                tot_estimate = amt
                print('Amount to pay : ', round(amt,2))


        print('--------------------------------------------------------------------------------------')
        
        r = receipt(meterread_data[m].MeterID,meterread_data[m].MeterID.ReadingAreaNo,meterread_data[m].ReadingYYYY,meterread_data[m].ProcessingMM,kbntype,ppu,shareval,tot_estimate)
        ls.append(r)

    context = {

        'values' : ls        
    }

    print('list set is' , ls)
    return render(request,'receipt/home.html' , context)