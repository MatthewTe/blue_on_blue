from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("vertical_video/", include("vertical_video.urls"))

]
