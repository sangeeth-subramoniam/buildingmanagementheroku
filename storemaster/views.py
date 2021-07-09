from django.shortcuts import render,redirect
from structure.models import StoreMaster
from .forms import StoreMasterForm

# Create your views here.
def home(request):

    form = StoreMasterForm()
    if(request.method == 'POST'):
        form = StoreMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/storemaster')

    storemaster = StoreMaster.objects.all().order_by('StoreNO')

    context = {
        'form' : form,
        'storemaster' : storemaster
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

