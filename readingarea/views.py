import readingarea
from django.shortcuts import render,redirect
from structure.models import *
from .forms import ReadingAreaForm,AreaSearchForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    form = ReadingAreaForm()
    searchform = AreaSearchForm()
    if(request.method == 'POST'):
        form = ReadingAreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/readingarea')

    
    delflg = request.GET.get('DeleteFlg') 
    readingarea = ReadingArea.objects.all().order_by('ReadingAreaNo','ReadingAreaNM')
    print('del flag is ' , delflg)
    if(delflg != '' and delflg is not None):
        readingarea = readingarea.filter(DeleteFlg = 0)
    else:
        readingarea = readingarea.filter(DeleteFlg__in = [0,1])


    per_page = 20
    area_paginator = Paginator(readingarea , per_page)
    page_num = request.GET.get('page')
    area_page = area_paginator.get_page(page_num)

    context = { 
        'readingarea' : area_page ,
        'form' : form ,
        'pgcount' : area_paginator.num_pages,
        'per_page' : per_page,
        'searchform' : searchform,
    }

    return render(request,'readingarea/home.html', context )

def updateReadingForm(request , pk):
    readingarea = ReadingArea.objects.get(ReadingAreaNo = pk)
    form = ReadingAreaForm( instance=readingarea)

    if(request.method == 'POST'):
        #print('Contents' , request.POST)
        if 'submit' in request.POST:
            form = ReadingAreaForm(request.POST , instance=readingarea)
            if form.is_valid():
                form.save()
                return redirect('/readingarea')
        else:
            return redirect('/readingarea')



    context = {
        'form' : form
    }

    return render(request,'readingarea/update_form.html',context)

def deleteReadingForm(request, pk):

    readingarea = ReadingArea.objects.get(ReadingAreaNo = pk)

    if(request.method == 'POST'):
        readingarea.delete()
        return redirect('/readingarea')


    context = {
        'ra' : readingarea
    }

    return render(request, 'readingarea/delete_form.html' , context)