

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