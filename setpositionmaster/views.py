from django.shortcuts import render,redirect
from structure.models import SetPositionMaster
from .forms import SetPositionMasterForm

# Create your views here.
def home(request):

    form = SetPositionMasterForm()
    if(request.method == 'POST'):
        form = SetPositionMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/setpositionmaster')

    setposition = SetPositionMaster.objects.all().order_by('ReadingAreaNo')

    context = {
        'form' : form,
        'setposition' : setposition
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

