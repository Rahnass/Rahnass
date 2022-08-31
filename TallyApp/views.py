from asyncio.windows_events import NULL
from django.shortcuts import render,redirect
from django.contrib import messages
from TallyApp.models import Ledger,  MainGroup, Print_Cheque, SubGroup ,Under, lbank, lcheque

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
    return render(request, 'main_group.html')       

def sub_grp_alter(request,pk):
    if request.method=='POST':
        sgrp =SubGroup.objects.get(id=pk)
        sgrp.name = request.POST.get('name')
        sgrp.alias = request.POST.get('alias')
        sgrp.group = request.POST.get('grp')
        sgrp.nett_balance = request.POST.get('nett')
        sgrp.used_for = request.POST.get('used')
        sgrp.method = request.POST.get('method')
        
        
        sgrp.save()
        return redirect('groups')
    return render(request, 'sub_group.html')  

def ledgers(request):
    grpp=Under.objects.all()
    context={'grpp':grpp}
    return render(request, 'ledgers.html',context=context)      


def ledger_alter(request,pk):
    grpp=Ledger.objects.get(id=pk)
    context={'a':grpp}
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

        led.mail_name = request.POST.get('name', False)
        led.mail_address = request.POST.get('address', False)
        led.mail_state = request.POST.get('state', False)
        led.mail_country = request.POST.get('country', False)
        led.mail_pincode = request.POST.get('pincode', False)

        led.bank_od_limit = request.POST.get('od_limit', False)
        led.bank_holder_name =request.POST.get('holder_name', False)
        led.bank_ac_number = request.POST.get('ac_number', False)
        led.bank_ifsc = request.POST.get('ifsc', False)
        led.bank_swift_code =request.POST.get('swift_code', False)
        led.bank_bank_name = request.POST.get('bank_name', False)
        led.bank_branch_name = request.POST.get('branch_name', False)
        led.bank_alter_chk_bks =request.POST.get('alter_chk_bks', False)
        led.bank_enbl_chk_printing = request.POST.get('enbl_chk_printing', False)

        led.tax_gst_uin = request.POST.get('gst_uin', False)
        led.tax_register_type = request.POST.get('register_type', False)
        led.tax_pan_no = request.POST.get('pan_no', False)
        led.tax_alter_gst_details =request.POST.get('alter_gst_details', False)

        led.sta_assessable_calculation = request.POST.get('assessable_calculation', False)
        led.sta_Appropriate_to =request.POST.get('Appropriate_to', False)
        led.sta_gst_applicable = request.POST.get('is_gst_applicable',False)
        led.sta_Set_alter_GST =request.POST.get('Set_alter_GST', False)
        led.sta_type_of_supply = request.POST.get('type_of_supply',False)
        led.sta_Method_of_calc =request.POST.get('Method_of_calc', False)

        led.rou_Rounding_Method = request.POST.get('Rounding_Method', False)
        led.rou_Round_limit  = request.POST.get('Round_limit', False)

        led.ta_type_of_duty_or_tax =request.POST.get('type_of_duty_or_tax', False)
        led.ta_type_of_tax =request.POST.get('type_of_tax', False)
        led.ta_valuation_type =request.POST.get('valuation_type', False)
        led.ta_rate_per_unit =request.POST.get('rate_per_unit', False)
        led.ta_Persentage_of_calculation =request.POST.get('Persentage_of_calculation', False)

        led.sun_maintain_balance_bill_by_bill =request.POST.get('maintain_balance_bill_by_bill', False)
        led.sun_Default_credit_period =request.POST.get('Default_credit_period', False)
        led.sun_Check_for_credit_days =request.POST.get('Check_for_credit_days', False) 

        led.save()
        return redirect('ledgers')
    return render(request,'ledger_alter.html')


def ledger_bank_details(request,pk):
    bnk=Ledger.objects.get(id=pk)
    bnn=lbank.objects.filter(ledger_id=bnk.id)
    context = {'a':bnk,'bnn':bnn}
    return render(request,'l_bank_details.html',context)

def add_bank_details(request,pk):
    if request.method == 'POST':
        bb = Ledger.objects.get(id=pk)
        abtype = request.POST.get('ttype',False)
        abcross = request.POST.get('cross',False)
        abacno = request.POST['acno']
        abifsc = request.POST.get('ifsc',False)
        abbname = request.POST.get('bankname',False)

        lbnk = lbank(ledger_id_id=bb.id,transaction_type=abtype,cross_using=abcross,acno=abacno,ifscode=abifsc,bankname=abbname)
        lbnk.save()
        context = {'bb':bb}
        return render(request, 'l_bank_details.html',context)   
    return render(request, 'ledgers.html')         

def ledger_cheque_details(request,pk):
    bnk=Ledger.objects.get(id=pk)
    context = {'a':bnk}
    return render(request,'l_cheque_range.html',context)

def add_cheque_details(request,id):
    if request.method == 'POST':
        cc = Ledger.objects.get(id=id)
        fromno = request.POST.get("fno")
        tono = request.POST.get("tno")
        numc = request.POST.get("noc")
        namec = request.POST.get("nac")

        lchq = lcheque(ledger_id=cc,from_no=fromno,to_no=tono,no_cheques=numc,name_cheque=namec)
        lchq.save()
        return render(request,'l_cheque_range.html')
    return render('ledgers.html')    

def cheque_printing(request,pk):
    bnk=Ledger.objects.get(id=pk)
    context = {'a':bnk}
    return render(request,'cheque_printing.html',context)

def add_cheque_dimensions(request,id):
    if request.method == 'POST':
        cpp = Ledger.objects.get(id=id)
        cwidth = request.POST.get("widthc",False)
        cheight = request.POST.get("heightc",False)

        ccsl = request.POST.get("start_left",False)
        ccst = request.POST.get("start_top",False)

        cddl = request.POST.get("dist_left",False)
        cddt = request.POST.get("dist_top",False)
        cdstyl = request.POST.get("datec",False)
        cdsep = request.POST.get("seperator_d",False)
        cdsepwidth = request.POST.get("sep_width",False)
        cdsepdist = request.POST.get("sep_dist",False)

        ppdl = request.POST.get("p_dist_left",False)
        ppdt = request.POST.get("p_dist_top",False)
        ppwidth = request.POST.get("p_width_area",False)

        amtdt = request.POST.get("a_dist_2",False)
        amthg = request.POST.get("a_height_2")
        amtdtt = request.POST.get("a_dist_3")
        amtstl = request.POST.get("a_start_left")
        amtstll = request.POST.get("a_start_2")
        amtwidth = request.POST.get("a_width")
        amtcur = request.POST.get("a_currency")

        cmpname = request.POST.get("com_name",False)
        pcmpname = request.POST.get("c_name",False)
        signf = request.POST.get("1_sign",False)
        signs = request.POST.get("2_sign",False)
        signdt = request.POST.get("s_dist_topp",False)
        signsl = request.POST.get("s_dist_leftt",False)
        signwidth = request.POST.get("sign_width",False)
        signheight = request.POST.get("sign_height",False)


        prchq = Print_Cheque(ledger_id=cpp,
                               cheque_width=cwidth,
                               cheque_height=cheight,
                               cc_start_left=ccsl,
                               cc_start_top=ccst,
                               cdate_dist_left=cddl,
                               cdate_dist_top=cddt,
                               date_style=cdstyl,
                               date_seprator=cdsep,
                               date_sep_width=cdsepwidth,
                               date_dist=cdsepdist,
                               party_dist_left=ppdl,
                               party_dist_top=ppdt,
                               party_width=ppwidth,
                               amount_dist_top=amtdt,
                               amount_height_gap=amthg,
                               amount_dist2_top=amtdtt,
                               amount_start1_left=amtstl,
                               amount_start2_left=amtstll,
                               amount_width=amtwidth,
                               amount_currency=amtcur,
                               company_name=cmpname,
                               print_cname=pcmpname,
                               sign_first=signf,
                               sign_second=signs,
                               sign_dist_top=signdt,
                               sign_start_left=signsl,
                               sign_width=signwidth,
                               sign_height=signheight)
        prchq.save()
        return render(request,'c_print.html')
    return render('cheque_printing.html')        

def c_print(request,pk):
    bnk=Print_Cheque.objects.get(id=pk)
    context = {'a':bnk}
    return render(request,'c_print.html',context)