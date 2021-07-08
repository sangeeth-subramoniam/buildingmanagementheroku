import readingarea
from django.shortcuts import render,redirect
from structure.models import *
from .forms import ReadingAreaForm

# Create your views here.
def home(request):
    form = ReadingAreaForm()
    if(request.method == 'POST'):
        form = ReadingAreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/readingarea')

    
    
    readingarea = ReadingArea.objects.all().order_by('ReadingAreaNo','ReadingAreaNM')

    context = { 
        'readingarea' : readingarea ,
        'form' : form ,
    }

    return render(request,'readingarea/home.html', context )

def updateReadingForm(request , pk):
    readingarea = ReadingArea.objects.get(ReadingAreaNo = pk)
    form = ReadingAreaForm( instance=readingarea)

    if(request.method == 'POST'):
        form = ReadingAreaForm(request.POST , instance=readingarea)
        if form.is_valid():
            form.save()
            return redirect('/readingarea')


    context = {
        'form' : form
    }

    return render(request,'readingarea/update_form.html',context)

def deleteReadingForm(request, pk):

    readingarea = ReadingArea.objects.get(ReadingAreaNo = pk)

    if(request.method == 'POST'):
        readingarea.delete(readingarea)
        return redirect('/readingarea')


    context = {
        'ra' : readingarea
    }

    return render(request, 'readingarea/delete_form.html' , context)