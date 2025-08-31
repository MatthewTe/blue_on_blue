from django.shortcuts import render

from vertical_video.models import VerticalVideo

def index(request):

    all_videos = VerticalVideo.objects.all()

    return render(request, "index.html", {"videos": all_videos})