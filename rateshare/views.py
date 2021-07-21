from django.shortcuts import render,redirect
from structure.models import MeterMaster, RateShare, ReadingArea , StoreMaster
from .forms import RateSharingForm , RateSharingUpdateForm ,RateSearchForm 
from django.core.paginator import Paginator

# Create your views here.
def home(request):

    form = RateSharingForm()
    searchform = RateSearchForm()
    if(request.method == 'POST'):
        form = RateSharingForm(request.POST)
        print('the form data is ' , request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rateshare')

    print('brfore params')
    ProcessingYYYY = request.GET.get('ProcessingYYYY')
    if(ProcessingYYYY == '' or ProcessingYYYY is None):
        ProcessingYYYY = 0
    ProcessingMM = request.GET.get('ProcessingMM')
    if(ProcessingMM == '' or ProcessingMM == None):
        ProcessingMM = 0
    ReadingArean = request.GET.get('ReadingAreaNo2')
    if(ReadingArean == '' or ReadingArean == None):
        ReadingArean = 0
    MeterKBN2 = request.GET.get('MeterKBN2')
    if(MeterKBN2 == '' or MeterKBN2 == None):
        MeterKBN2 = 0
    MeterID2 = request.GET.get('MeterID2')
    if(MeterID2 == '' or MeterID2 == None):
        MeterID2 = 0
    DeleteFlg = request.GET.get('DeleteFlg')
    if(DeleteFlg == '' or DeleteFlg == None):
        DeleteFlg = 0


    rate_share_meter = RateShare.objects.all().order_by('MeterID')
    rate_share_meter.group_by = ['ProcessingYYYY' , 'ProcessingMM']

    

    print('values are ' , rate_share_meter)

    if(ProcessingYYYY != 0):
        rate_share_meter = rate_share_meter.filter(ProcessingYYYY = ProcessingYYYY)

    print('after filtering reading yyyy ', rate_share_meter)

    if(ProcessingMM != 0):
        rate_share_meter = rate_share_meter.filter(ProcessingMM = ProcessingMM)
        print('after filtering reading mm ', rate_share_meter)

    if(ReadingArean != 0):
        rate_share_meter = rate_share_meter.filter(StoreNO__ReadingAreaNo = ReadingArean)
        print('after filtering reading area ', rate_share_meter)

    if(MeterID2 != 0):
        rate_share_meter = rate_share_meter.filter(MeterID = MeterID2)
        print('after filtering MeterID ', rate_share_meter)


    print('rate share meter after filter is ' , rate_share_meter)

    #Paginator
    per_page = 5
    Share_paginator = Paginator(rate_share_meter , per_page)
    page_num = request.GET.get('page')
    share_page = Share_paginator.get_page(page_num)

    

    context = { 
        'form' : form,
        'rate_share_meter' : share_page ,
        'pgcount' : Share_paginator.num_pages,
        'per_page' : per_page,
        'searchform' : searchform,

    }

    return render(request,'rateshare/home.html' , context)

def updaterateForm(request , pk):
    rate = RateShare.objects.get(id = pk)
    form = RateSharingUpdateForm(instance=rate)

    if(request.method == 'POST'):
        #print('Contents' , request.POST)
        if 'submit' in request.POST:
            form = RateSharingUpdateForm(request.POST , instance=rate)
            if form.is_valid():
                form.save()
                return redirect('/rateshare')
        else:
            return redirect('/rateshare')
    
    context = {
        'form' : form
    }

    return render(request,'rateshare/update_form.html',context)

def deleterateForm(request, pk):

    rateshare = RateShare.objects.get(id = pk)

    if(request.method == 'POST'):
        rateshare.delete()
        return redirect('/rateshare')


    context = {
        'rs' : rateshare
    }

    return render(request, 'rateshare/delete_form.html' , context)



def load_store(request):
    ReadingAreaNo_id = request.GET.get('ReadingArea')
    print('test1')
    MeterKBN = request.GET.get('MeterKBN')
    print('3nded')
    if(MeterKBN == ''):
        MeterKBN = 0    
    print('mk is ',MeterKBN)
    stores = StoreMaster.objects.filter(ReadingAreaNo_id=ReadingAreaNo_id).order_by('StoreNO')
    meters = MeterMaster.objects.filter(ReadingAreaNo_id=ReadingAreaNo_id  , MeterKBN = MeterKBN ).order_by('MeterID')
    print('process ended')
    return render(request, 'rateshare/store_dropdown_list_options.html', {'stores': stores , 'meters' : meters})

def load_meters(request):
    
    ReadingAreaNo_id = request.GET.get('ReadingArea')
    
    MeterKBN = request.GET.get('MeterKBN')
    print('kbn is' , MeterKBN)
    
    meters = MeterMaster.objects.filter(ReadingAreaNo_id=ReadingAreaNo_id , MeterKBN = MeterKBN).order_by('MeterID')
    print('meters are' , meters)
    
    return render(request, 'rateshare/meter_dropdown_list_options.html', {'meters': meters})