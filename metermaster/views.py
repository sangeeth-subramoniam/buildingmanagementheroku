from django.shortcuts import render,redirect
from structure.models import MeterMaster, ReadingArea, StoreMaster
from .forms import MeterMasterForm,MeterSearchForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):

    form = MeterMasterForm()
    searchform = MeterSearchForm()
    if(request.method == 'POST'):
        form = MeterMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/metermaster')

    ReadingArean = request.GET.get('ReadingAreaNo')
    MeterKBN = request.GET.get('MeterKBN')
    UseType = request.GET.get('UseType')
    DeleteFlg = request.GET.get('DeleteFlg') 

    meter = MeterMaster.objects.all().order_by('MeterNo')

    if(ReadingArean != '' and ReadingArean is not None):
        meter = meter.filter(ReadingAreaNo = ReadingArean)

    if(MeterKBN != '' and MeterKBN is not None):
        meter = meter.filter(MeterKBN = MeterKBN)
    
    if(UseType != '' and UseType is not None):
        meter = meter.filter(UseType = UseType)

    if(DeleteFlg != '' and DeleteFlg is not None):
        meter = meter.filter(DeleteFlg = 0 )
    else:
        meter = meter.filter(DeleteFlg__in = [0,1] )

    
    #Paginator
    per_page = 5
    Meter_paginator = Paginator(meter , per_page)
    page_num = request.GET.get('page')
    meter_page = Meter_paginator.get_page(page_num)

    context = {
        'form' : form,
        'meter' : meter_page,
        'pgcount' : Meter_paginator.num_pages,
        'per_page' : per_page,
        'searchform' : searchform,

    }
    return render(request,'metermaster/home.html' , context)

def updatemeterForm(request , pk):
    meter = MeterMaster.objects.get(id = pk)
    form = MeterMasterForm( instance=meter)

    if(request.method == 'POST'):
        #print('Contents' , request.POST)
        if 'submit' in request.POST:
            form = MeterMasterForm(request.POST , instance=meter)
            if form.is_valid():
                form.save()
                return redirect('/metermaster')
        else:
            return redirect('/metermaster')
    
    context = {
        'form' : form
    }

    return render(request,'metermaster/update_form.html',context)

def deletemeterForm(request, pk):

    meter = MeterMaster.objects.get(id = pk)

    if(request.method == 'POST'):
        meter.delete()
        return redirect('/metermaster')


    context = {
        'mm' : meter
    }

    return render(request, 'metermaster/delete_form.html' , context)


def load_store(request):
    ReadingAreaNo_id = request.GET.get('ReadingArea')
    print('entering ajax value is ', ReadingAreaNo_id)
    stores = StoreMaster.objects.filter(ReadingAreaNo_id=ReadingAreaNo_id).order_by('StoreNO')
    print('stores are ', stores)
    return render(request, 'metermaster/store_dropdown_list_options.html', {'stores': stores})

