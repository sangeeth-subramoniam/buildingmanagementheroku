from django.shortcuts import render,redirect
from structure.models import Price
from .forms import SetPriceForm,SetPriceSearchForm
from django.core.paginator import Paginator
from django.db.models import  Sum, Q , F
from django.db import models
# Create your views here.
def home(request):

    form = SetPriceForm()
    searchform = SetPriceSearchForm()
    if(request.method == 'POST'):
        form = SetPriceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/adjustment')

    processingYYYY = request.GET.get('ProcessingYYYY')
    processingMM = request.GET.get('ProcessingMM')

    setprice = Price.objects.all().order_by('ReadingAreaNo' ).annotate(total=Sum(
                    (F('ElectricPrice') - F('ElectricAdjustment')) + 
                    (F('GasPrice') - F('GasAdjustment')) +
                    (F('WaterPrice') - F('WaterAdjustment')) ,   
                    output_field= models.FloatField()
                ))

    if(processingYYYY != '' and processingYYYY is not None):
        setprice = setprice.filter(ProcessingYYYY = processingYYYY )

    if(processingMM != '' and processingMM is not None):
        setprice = setprice.filter(ProcessingMM = processingMM )
    

    per_page = 5
    price_paginator = Paginator(setprice , per_page)
    page_num = request.GET.get('page')
    Price_page = price_paginator.get_page(page_num)

    print('tret' , setprice[0].total)



    context = {
        'form' : form,
        'setprice' : Price_page,
        'pgcount' : price_paginator.num_pages,
        'per_page' : per_page,
        'searchform' : searchform,

    }
    return render(request,'adjustment/home.html' , context)


def updateadjustmentForm(request , pk):
    setprice = Price.objects.get(id = pk)
    form = SetPriceForm(instance=setprice)
    #form.fields['ReadingAreaNo'].disabled = True
    #form.fields['ProcessingYYYY'].disabled = True 
    #form.fields['ProcessingMM'].disabled = True 
    #form.fields['ElectricPrice'].disabled = True 
    #form.fields['GasPrice'].disabled = True 
    #form.fields['WaterPrice'].disabled = True 


    if(request.method == 'POST'):
        #print('Contents' , request.POST)
        if 'submit' in request.POST:
            form = SetPriceForm(request.POST , instance=setprice)
            if form.is_valid():
                form.save()
                return redirect('/adjustment')
        else:
            return redirect('/adjustment')
    
    context = {
        'form' : form
    }

    return render(request,'adjustment/update_form.html',context)

def deleteadjustmentForm(request, pk):

    setprice = Price.objects.get(id = pk)

    if(request.method == 'POST'):
        setprice.delete()
        return redirect('/adjustment')


    context = {
        'sp' : setprice
    }

    return render(request, 'adjustment/delete_form.html' , context)

