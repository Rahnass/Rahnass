from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def groups(request):
    return render(request,'groups.html')    

def main_group(request):
    return render(request,'main_group.html')     
    
def ledgers(request):
    return render(request,'ledgers.html')         