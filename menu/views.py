from django.shortcuts import render

# Create your views here.
def menu_home(request):
    context= {
        'test' : 'sangeeth'
    }
    return render(request,"menu/menu_home.html" , context)
