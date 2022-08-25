from django.shortcuts import render,redirect

from TallyApp.models import Ledger, MainGroup, SubGroup ,Under

# Create your views here.
def home(request):
    return render(request,'home.html')

def groups(request):
    grp=MainGroup.objects.all()
    context={'grp':grp}
    return render(request, 'groups.html',context)   

def m_group(request,pk):
    grp=MainGroup.objects.get(id=pk)
    return render(request, 'main_group.html',{'a':grp})   
    
def s_group(request,pk):
    grps=SubGroup.objects.get(id=pk)
    return render(request, 'sub_group.html',{'a':grps})  

def ledgers(request):
    return render(request,'ledgers.html')      

def grp_alter(request,pk):
    if request.method=='POST':
        grp =MainGroup.objects.get(id=pk)
        grp.name = request.POST.get('name')
        grp.alias = request.POST.get('alias')
        grp.group = request.POST.get('grp')
        grp.nett_balance = request.POST.get('nett')
        grp.used_for = request.POST.get('used')
        grp.method = request.POST.get('method')
        
        
        grp.save()
        return redirect('groups')
    return render(request, 'main_group.html',)       

def ledgers(request):
    grpp=Under.objects.all()
    context={'grpp':grpp}
    return render(request, 'ledgers.html',context)      


def ledger_alter(request,pk):
    grpp=Ledger.objects.get(id=pk)
    return render(request, 'ledger_alter.html',{'a':grpp})  
