from django.shortcuts import render,redirect
from django.contrib import messages
from TallyApp.models import L_Tax_Register, Ledger, Ledger_Banking_Details, Ledger_Mailing_Address, Ledger_Rounding, Ledger_Satutory, Ledger_sundry, Ledger_tax,  MainGroup, SubGroup ,Under

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
    return render(request, 'ledgers.html',context=context)      


def ledger_alter(request,pk):
    grpp=Ledger.objects.get(id=pk)
    gr=Ledger_Mailing_Address.objects.filter(ledger_id=grpp)
    context={'gr':gr}
    return render(request, 'ledger_alter.html',context)  


def alter_ledger(request,pk):
    if request.method == 'POST':
        #ledm = Ledger_Mailing_Address.objects.get(id=pk)
        led =Ledger.objects.get(id=pk)
        led.ledger_name = request.POST.get('ledger_name')
        led.ledger_alias = request.POST.get('ledger_alias', False)
        led.ledger_opening_bal = request.POST.get('ledger_opening_bal', False)
        led.ledger_type = request.POST.get('ledger_type', False)
        led.subgroup_name = request.POST.get('group_under',False)

        led.save()
        idd = led.id

        ledm = Ledger_Mailing_Address.objects.get(id=pk)
        ledm.name = request.POST.get('name', False)
        ledm.address = request.POST.get('address', False)
        ledm.state = request.POST.get('state', False)
        ledm.country = request.POST.get('country', False)
        ledm.pincode = request.POST.get('pincode', False)

        ledm.save()

        ledb = Ledger_Banking_Details.objects.get(id=idd)
        ledb.od_limit = request.POST.get('od_limit', False)
        ledb.holder_name =request.POST.get('holder_name', False)
        ledb.ac_number = request.POST.get('ac_number', False)
        ledb.ifsc = request.POST.get('ifsc', False)
        ledb.swift_code =request.POST.get('swift_code', False)
        ledb.bank_name = request.POST.get('bank_name', False)
        ledb.branch_name = request.POST.get('branch_name', False)
        ledb.alter_chk_bks =request.POST.get('alter_chk_bks', False)
        ledb.enbl_chk_printing = request.POST.get('enbl_chk_printing', False) 

        ledb.save()

        ledt = L_Tax_Register.objects.get(id=idd)
        ledt.gst_uin = request.POST.get('gst_uin', False)
        ledt.register_type = request.POST.get('register_type', False)
        ledt.pan_no = request.POST.get('pan_no', False)
        ledt.alter_gst_details =request.POST.get('alter_gst_details', False)

        ledt.save()

        leds = Ledger_Satutory.objects.get(id=idd)
        leds.assessable_calculation = request.POST.get('assessable_calculation', False)
        leds.Appropriate_to =request.POST.get('Appropriate_to', False)
        leds.gst_applicable = request.POST.get('is_gst_applicable',False)
        leds.Set_alter_GST =request.POST.get('Set_alter_GST', False)
        leds.type_of_supply = request.POST.get('type_of_supply',False)
        leds.Method_of_calc =request.POST.get('Method_of_calc', False)

        leds.save()

        ledr = Ledger_Rounding.objects.get(id=idd)
        ledr.Rounding_Method = request.POST.get('Rounding_Method', False)
        ledr.Round_limit  = request.POST.get('Round_limit', False)

        ledr.save()
        
        ledtax = Ledger_tax.objects.get(id=idd)
        ledtax.type_of_duty_or_tax =request.POST.get('type_of_duty_or_tax', False)
        ledtax.type_of_tax =request.POST.get('type_of_tax', False)
        ledtax.valuation_type =request.POST.get('valuation_type', False)
        ledtax.rate_per_unit =request.POST.get('rate_per_unit', False)
        ledtax.Persentage_of_calculation =request.POST.get('Persentage_of_calculation', False)

        ledtax.save()

        ledsun = Ledger_sundry.objects.get(id=idd)
        ledsun.maintain_balance_bill_by_bill =request.POST.get('maintain_balance_bill_by_bill', False)
        ledsun.Default_credit_period =request.POST.get('Default_credit_period', False)
        ledsun.Check_for_credit_days =request.POST.get('Check_for_credit_days', False)    

        ledsun.save() 

        return redirect('ledgers')
    return render(request,'ledger_alter.html')


def ledger_bank_details(request):
    return render(request,'l_bank_details.html')
