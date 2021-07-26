from django.shortcuts import render,redirect
from structure.models import Price
from .forms import SetPriceForm,SetPriceSearchForm
from django.core.paginator import Paginator
# Create your views here.
def home(request):

    form = SetPriceForm()
    searchform = SetPriceSearchForm()
    if(request.method == 'POST'):
        form = SetPriceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/setprice')

    processingYYYY = request.GET.get('ProcessingYYYY')
    processingMM = request.GET.get('ProcessingMM')

    setprice = Price.objects.all().order_by('ProcessingYYYY' , 'ProcessingMM' )

    if(processingYYYY != '' and processingYYYY is not None):
        setprice = setprice.filter(ProcessingYYYY = processingYYYY )

    if(processingMM != '' and processingMM is not None):
        setprice = setprice.filter(ProcessingMM = processingMM )
    

    per_page = 5
    price_paginator = Paginator(setprice , per_page)
    page_num = request.GET.get('page')
    Price_page = price_paginator.get_page(page_num)



    context = {
        'form' : form,
        'setprice' : Price_page,
        'pgcount' : price_paginator.num_pages,
        'per_page' : per_page,
        'searchform' : searchform,
    }
    return render(request,'setprice/home.html' , context)


def updateSetPriceForm(request , pk):
    setprice = Price.objects.get(id = pk)
    form = SetPriceForm( instance=setprice)

    if(request.method == 'POST'):
        #print('Contents' , request.POST)
        if 'submit' in request.POST:
            form = SetPriceForm(request.POST , instance=setprice)
            if form.is_valid():
                form.save()
                return redirect('/setprice')
        else:
            return redirect('/setprice')
    
    context = {
        'form' : form
    }

    return render(request,'setprice/update_form.html',context)

def deleteSetPriceForm(request, pk):

    setprice = Price.objects.get(id = pk)

    if(request.method == 'POST'):
        setprice.delete()
        return redirect('/setprice')


    context = {
        'sp' : setprice
    }

    return render(request, 'setprice/delete_form.html' , context)

