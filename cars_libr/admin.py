from django.contrib import admin


from .models import Car, UserProfile

admin.site.register(
    (Car)
)

@admin.register(UserProfile)  
class ProfileAdmin(admin.ModelAdmin):  
    pass
