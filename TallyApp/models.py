

from statistics import mode
from django.db import models

# Create your models here.

class Under(models.Model):
    cat_name=models.CharField(max_length=100)
 
    def __str__(self):
        return self.cat_name

class MainGroup(models.Model):
    under=models.ForeignKey(Under,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225,blank=True)
    under_group=models.CharField(max_length=225)
    affect_gp=models.CharField(max_length=255,blank=True)
    group=models.CharField(max_length=225)
    nett_balance=models.CharField(max_length=225)
    used_for=models.CharField(max_length=225)
    method=models.CharField(max_length=225)


    def __str__(self):
        return self.name

class SubGroup(models.Model):
    maingroup=models.ForeignKey(MainGroup,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225,blank=True)
    group=models.CharField(max_length=225)
    nett_balance=models.CharField(max_length=225)
    used_for=models.CharField(max_length=225)
    method=models.CharField(max_length=225)    

    
    def __str__(self):
        return self.name


class Ledger(models.Model):
    subgroup=models.ForeignKey(SubGroup,null=True,on_delete=models.CASCADE)
    ledger_name = models.CharField(max_length=225,default="Null",blank=True)
    ledger_alias = models.CharField(max_length=225,default="Null",blank=True)
    ledger_opening_bal = models.CharField(max_length=225,default="Null",blank=True)
    ledger_type = models.CharField(max_length=225,default="Null",blank=True)

    tax_gst_uin = models.CharField(max_length=225,default="Null",blank=True)
    tax_register_type =models.CharField(max_length=225,default="Null",blank=True)
    tax_pan_no = models.CharField(max_length=225,default="Null",blank=True)
    tax_alter_gst_details = models.CharField(max_length=225,default="Null",blank=True)

    sta_assessable_calculation = models.CharField(max_length=225,default="Null",blank=True)
    sta_Appropriate_to =models.CharField(max_length=225,default="Null",blank=True)
    sta_gst_applicable = models.CharField(max_length=225,default="Null",blank=True)
    sta_Set_alter_GST =models.CharField(max_length=225,default="Null",blank=True)
    sta_type_of_supply = models.CharField(max_length=225,default="Null",blank=True)
    sta_Method_of_calc=models.CharField(max_length=225,default="Null",blank=True)

    rou_Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    rou_Round_limit = models.CharField(max_length=22,default="Null",blank=True)

    ta_type_of_duty_or_tax =models.CharField(max_length=225,default="Null",blank=True)
    ta_type_of_tax =models.CharField(max_length=225,default="Null",blank=True)
    ta_valuation_type=models.CharField(max_length=225,default="Null",blank=True)
    ta_rate_per_unit =models.CharField(max_length=225,default="Null",blank=True)
    ta_Persentage_of_calculation=models.CharField(max_length=225,default="Null",blank=True)

    sun_maintain_balance_bill_by_bill =models.CharField(max_length=225,default="Null",blank=True)
    sun_Default_credit_period=models.CharField(max_length=225,default="Null",blank=True)
    sun_Check_for_credit_days=models.CharField(max_length=225,default="Null",blank=True)

    bank_od_limit = models.CharField(max_length=225,default="Null",blank=True)
    bank_holder_name =models.CharField(max_length=225,default="Null",blank=True)
    bank_ac_number =models.CharField(max_length=225,default="Null",blank=True)
    bank_ifsc =models.CharField(max_length=225,default="Null",blank=True)
    bank_swift_code =models.CharField(max_length=225,default="Null",blank=True)
    bank_bank_name = models.CharField(max_length=225,default="Null",blank=True)
    bank_branch_name = models.CharField(max_length=225,default="Null",blank=True)
    bank_alter_chk_bks =  models.CharField(max_length=225,default="Null",blank=True)
    bank_enbl_chk_printing =  models.CharField(max_length=225,default="Null",blank=True)
    bank_auto_recoun= models.CharField(max_length=225,default="Null",blank=True)

    mail_name = models.CharField(max_length=225,default="Null",blank=True)
    mail_address = models.CharField(max_length=225,default="Null",blank=True)
    mail_state = models.CharField(max_length=225,default="Null",blank=True)
    mail_country =models.CharField(max_length=225,default="Null",blank=True)
    mail_pincode =models.CharField(max_length=225,default="Null",blank=True)

    def __str__(self):
        return self.ledger_name
        


class lbank(models.Model):
    ledger_id=models.OneToOneField(Ledger,on_delete=models.CASCADE)
    transaction_type=models.CharField(max_length=100,blank=True,default="Null")
    cross_using=models.CharField(max_length=200,blank=True,default="Null")
    acno=models.CharField(max_length=100,blank=True,default="Null")
    ifscode = models.CharField(max_length=200,blank=True,default="Null")
    bankname = models.CharField(max_length=200,blank=True,default="Null")

class lcheque(models.Model):
    ledger_id=models.ForeignKey(Ledger,on_delete=models.CASCADE)
    from_no=models.CharField(max_length=100,blank=False)
    to_no=models.CharField(max_length=100,blank=False)
    no_cheques=models.CharField(max_length=100,blank=False)
    name_cheque=models.CharField(max_length=100,blank=False)

class Print_Cheque(models.Model):
    ledger_id=models.OneToOneField(Ledger,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100,blank=False)
    payee_name=models.CharField(max_length=100,blank=False)

    cheque_number=models.CharField(max_length=100,blank=False)
    cheque_date=models.CharField(max_length=100,blank=False)

    amt_words=models.CharField(max_length=100,blank=False)
    amt_number=models.CharField(max_length=100,blank=False)

    

