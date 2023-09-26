from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import VideoModel

# Register your models here.

class videoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(VideoModel, videoAdmin)
