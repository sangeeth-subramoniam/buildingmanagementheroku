from django.shortcuts import render,redirect
from structure.models import StoreMaster
from .forms import StoreMasterForm,StoreSearchForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):

    form = StoreMasterForm()
    searchform = StoreSearchForm()
    if(request.method == 'POST'):
        form = StoreMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/storemaster')

    ReadingArea = request.GET.get('ReadingAreaNo')
    DeleteFlg = request.GET.get('DeleteFlg') 

    
    storemaster = StoreMaster.objects.all().order_by('StoreNO')

    if(ReadingArea != '' and ReadingArea is not None):
        storemaster = storemaster.filter(ReadingAreaNo = ReadingArea)

    if(DeleteFlg != '' and DeleteFlg is not None):
        storemaster = storemaster.filter(DeleteFlg = 0 )
    else:
        storemaster = storemaster.filter(DeleteFlg__in = [0,1] )

    per_page = 5
    Store_paginator = Paginator(storemaster , per_page)
    page_num = request.GET.get('page')
    store_page = Store_paginator.get_page(page_num)

    context = {
        'form' : form,
        'storemaster' : store_page,
        'pgcount' : Store_paginator.num_pages,
        'per_page' : per_page,
        'searchform' : searchform,
    }
    return render(request,'storemaster/home.html' , context)

def updateStoreForm(request , pk):
    storemaster = StoreMaster.objects.get(id = pk)
    form = StoreMasterForm( instance=storemaster)

    if(request.method == 'POST'):
        #print('Contents' , request.POST)
        if 'submit' in request.POST:
            form = StoreMasterForm(request.POST , instance=storemaster)
            if form.is_valid():
                form.save()
                return redirect('/storemaster')
        else:
            return redirect('/storemaster')
    
    context = {
        'form' : form
    }

    return render(request,'storemaster/update_form.html',context)

def deleteStoreForm(request, pk):

    storemaster = StoreMaster.objects.get(id = pk)

    if(request.method == 'POST'):
        storemaster.delete()
        return redirect('/storemaster')


    context = {
        'sm' : storemaster
    }

    return render(request, 'storemaster/delete_form.html' , context)

