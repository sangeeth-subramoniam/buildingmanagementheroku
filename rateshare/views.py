from django.shortcuts import render,redirect
from structure.models import MeterMaster, RateShare, ReadingArea , StoreMaster
from .forms import RateSharingForm

# Create your views here.
def home(request):

    form = RateSharingForm()
    if(request.method == 'POST'):
        form = RateSharingForm(request.POST)
        print('the form data is ' , request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rateshare')

    rate_share = RateShare.objects.all().order_by('MeterID')
    rate_share.group_by = ['MeterID']

    rate_share_meter = RateShare.objects.all().distinct('MeterID')

    context = { 
        'form' : form,
        'rate_share_meter' : rate_share_meter ,
        'rate_share' : rate_share ,
    }

    return render(request,'rateshare/home.html' , context)

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
    
    meters = MeterMaster.objects.filter(ReadingAreaNo_id=ReadingAreaNo_id , MeterKBN = MeterKBN).order_by('MeterID')
    
    return render(request, 'rateshare/meter_dropdown_list_options.html', {'meters': meters})