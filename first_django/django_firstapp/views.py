from django.shortcuts import render
from django.http import HttpResponse
from .models import VideoModel
from ipware import get_client_ip
import logging

# Create your views here.


logger = logging.getLogger(__name__)


def main(request):
    ip, is_routable = get_client_ip(request)
    videos = VideoModel.objects.all()
    context = {"video": videos}
    if is_routable:
        logger.info("Main page was visited by {ip}")
    else:
        logger.info("Hidden ip.")
    return render(request, "main.html", context)


def about(request):
    ip, is_routable = get_client_ip(request)
    if is_routable:
        logger.info(f"About page was visited by {ip}")
    else:
        logger.info("Hidden ip.")
    return render(request, "about.html")
