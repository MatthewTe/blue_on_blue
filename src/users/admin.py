from django.contrib import admin
from users.models import SocialMediaAccount

@admin.register(SocialMediaAccount)
class SocialMediaAccountAdmin(admin.ModelAdmin):
    pass
