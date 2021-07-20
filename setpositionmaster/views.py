from django.shortcuts import render,redirect
from structure.models import SetPositionMaster
from .forms import SetPositionMasterForm,SetPositionSearchForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):

    form = SetPositionMasterForm()
    searchform = SetPositionSearchForm()
    if(request.method == 'POST'):
        form = SetPositionMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/setpositionmaster')

    ReadingArea = request.GET.get('ReadingAreaNo')
    DeleteFlg = request.GET.get('DeleteFlg') 

    setposition = SetPositionMaster.objects.all().order_by('ReadingAreaNo')

    if(ReadingArea != '' and ReadingArea is not None):
        setposition = setposition.filter(ReadingAreaNo = ReadingArea)

    if(DeleteFlg != '' and DeleteFlg is not None):
        setposition = setposition.filter(DeleteFlg = 0 )
    else:
        setposition = setposition.filter(DeleteFlg__in = [0,1] )

    per_page = 5
    Position_paginator = Paginator(setposition , per_page)
    page_num = request.GET.get('page')
    Pos_page = Position_paginator.get_page(page_num)



    context = {
        'form' : form,
        'setposition' : Pos_page,
        'pgcount' : Position_paginator.num_pages,
        'per_page' : per_page,
        'searchform' : searchform,
    }
    return render(request,'setpositionmaster/home.html' , context)

def updatesetpositionForm(request , pk):
    setposition = SetPositionMaster.objects.get(id = pk)
    form = SetPositionMasterForm( instance=setposition)

    if(request.method == 'POST'):
        #print('Contents' , request.POST)
        if 'submit' in request.POST:
            form = SetPositionMasterForm(request.POST , instance=setposition)
            if form.is_valid():
                form.save()
                return redirect('/setpositionmaster')
        else:
            return redirect('/setpositionmaster')
    
    context = {
        'form' : form
    }

    return render(request,'setpositionmaster/update_form.html',context)

def deletesetpositionForm(request, pk):

    setposition = SetPositionMaster.objects.get(id = pk)

    if(request.method == 'POST'):
        setposition.delete()
        return redirect('/setpositionmaster')


    context = {
        'spm' : setposition
    }

    return render(request, 'setpositionmaster/delete_form.html' , context)

