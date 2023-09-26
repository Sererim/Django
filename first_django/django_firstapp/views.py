from django.shortcuts import render
from django.http import HttpResponse
from .models import VideoModel

# Create your views here.


def main(request):
    videos = VideoModel.objects.all()
    context = {"video": videos}
    return render(request, "main.html", context)


def about(request):
    return HttpResponse("NULL")
