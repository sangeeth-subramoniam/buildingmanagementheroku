from django.shortcuts import redirect, render
from structure.models import CodeMaster
from .forms import CodeMasterForm,CodeSearchForm
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    form = CodeMasterForm()
    searchform = CodeSearchForm()
    
    
    if(request.method == 'POST'):
        form = CodeMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/codemaster')

        
    codetype = request.GET.get('CodeType')    
    codemaster = CodeMaster.objects.all().order_by('Code')

    if(codetype != '' and codetype is not None):
        codemaster = codemaster.filter(id = codetype)
        

    per_page = 5
    code_paginator = Paginator(codemaster , per_page)

    
    page_num = request.GET.get('page')
    code_page = code_paginator.get_page(page_num)

    

    
    context = {
        'codemaster' : code_page,
        'form' : form,
        'pgcount' : code_paginator.num_pages,
        'per_page' : per_page,
        'searchform' : searchform,
    }
    return render(request, 'codemaster/home.html' , context)

def updateCodeForm(request , pk):
    codemaster = CodeMaster.objects.get(id = pk)
    form = CodeMasterForm( instance=codemaster)

    if(request.method == 'POST'):
        #print('Contents' , request.POST)
        if 'submit' in request.POST:
            form = CodeMasterForm(request.POST , instance=codemaster)
            if form.is_valid():
                form.save()
                return redirect('/codemaster')
        else:
            return redirect('/codemaster')
    
    context = {
        'form' : form
    }

    return render(request,'codemaster/update_form.html',context)

def deleteCodeForm(request, pk):

    codemaster = CodeMaster.objects.get(id = pk)

    if(request.method == 'POST'):
        codemaster.delete()
        return redirect('/codemaster')


    context = {
        'cm' : codemaster
    }

    return render(request, 'codemaster/delete_form.html' , context)