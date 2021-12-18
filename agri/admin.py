from django.contrib import admin
from .models import AgriUser,FarmerUser,GovempUser
# Register your models here.
admin.site.register(AgriUser)
admin.site.register(FarmerUser)
admin.site.register(GovempUser)