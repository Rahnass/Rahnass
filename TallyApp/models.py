

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

    def __str__(self):
        return self.ledger_name

class L_Tax_Register(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    gst_uin = models.CharField(max_length=225,default="Null",blank=True)
    register_type =models.CharField(max_length=225,default="Null",blank=True)
    pan_no = models.CharField(max_length=225,default="Null",blank=True)
    alter_gst_details = models.CharField(max_length=225,default="Null",blank=True)

    def __str__(self):
        return self.pan_no


class Ledger_Satutory(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    assessable_calculation = models.CharField(max_length=225,default="Null",blank=True)
    Appropriate_to =models.CharField(max_length=225,default="Null",blank=True)
    gst_applicable = models.CharField(max_length=225,default="Null",blank=True)
    Set_alter_GST =models.CharField(max_length=225,default="Null",blank=True)
    type_of_supply = models.CharField(max_length=225,default="Null",blank=True)
    Method_of_calc=models.CharField(max_length=225,default="Null",blank=True)

      



class Ledger_Rounding(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)

class Ledger_tax(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    type_of_duty_or_tax =models.CharField(max_length=225,default="Null",blank=True)
    type_of_tax =models.CharField(max_length=225,default="Null",blank=True)
    valuation_type=models.CharField(max_length=225,default="Null",blank=True)
    rate_per_unit =models.CharField(max_length=225,default="Null",blank=True)
    Persentage_of_calculation=models.CharField(max_length=225,default="Null",blank=True)
   

class Ledger_sundry(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    maintain_balance_bill_by_bill =models.CharField(max_length=225,default="Null",blank=True)
    Default_credit_period=models.CharField(max_length=225,default="Null",blank=True)
    Check_for_credit_days=models.CharField(max_length=225,default="Null",blank=True)
                


class Ledger_Banking_Details(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    od_limit = models.CharField(max_length=225,default="Null",blank=True)
    holder_name =models.CharField(max_length=225,default="Null",blank=True)
    ac_number =models.CharField(max_length=225,default="Null",blank=True)
    ifsc =models.CharField(max_length=225,default="Null",blank=True)
    swift_code =models.CharField(max_length=225,default="Null",blank=True)
    bank_name = models.CharField(max_length=225,default="Null",blank=True)
    branch_name = models.CharField(max_length=225,default="Null",blank=True)
    alter_chk_bks =  models.CharField(max_length=225,default="Null",blank=True)
    enbl_chk_printing =  models.CharField(max_length=225,default="Null",blank=True)
    auto_recoun= models.CharField(max_length=225,default="Null",blank=True)


    def __str__(self):
        return self.holder_name


class Ledger_Mailing_Address(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    ledger_bank = models.ForeignKey(Ledger_Banking_Details, on_delete=models.CASCADE, null=True, blank=True)
    ledger_tax = models.ForeignKey(L_Tax_Register, on_delete=models.CASCADE, null=True, blank=True)
    ledger_sat = models.ForeignKey(Ledger_Satutory,  on_delete=models.CASCADE,  null=True, blank=True)
    ledger_round = models.ForeignKey(Ledger_Rounding, on_delete=models.CASCADE, null=True, blank=True)
    l_tax = models.ForeignKey(Ledger_tax, on_delete=models.CASCADE, null=True, blank=True)
    l_sundry = models.ForeignKey(Ledger_sundry, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225,default="Null",blank=True)
    address = models.CharField(max_length=225,default="Null",blank=True)
    state = models.CharField(max_length=225,default="Null",blank=True)
    country =models.CharField(max_length=225,default="Null",blank=True)
    pincode =models.CharField(max_length=225,default="Null",blank=True)

    def __str__(self):
        return self.name


