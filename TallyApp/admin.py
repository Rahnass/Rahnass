from django.contrib import admin

from TallyApp.models import Ledger, MainGroup, SubGroup, Under



# Register your models here.


admin.site.register(Under)
admin.site.register(MainGroup)
admin.site.register(SubGroup)
admin.site.register(Ledger)
