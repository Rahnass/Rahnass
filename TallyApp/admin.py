from django.contrib import admin

from TallyApp.models import Ledger, Ledger_Banking_Details, Ledger_Mailing_Address, MainGroup, SubGroup, Under



# Register your models here.


admin.site.register(Under)
admin.site.register(MainGroup)
admin.site.register(SubGroup)
admin.site.register(Ledger)
admin.site.register(Ledger_Banking_Details)
admin.site.register(Ledger_Mailing_Address)
