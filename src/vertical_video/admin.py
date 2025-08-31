from django.contrib import admin
from vertical_video.models import VerticalVideo

# Register your models here.
@admin.register(VerticalVideo)
class VerticalVideoAdmin(admin.ModelAdmin):
    pass