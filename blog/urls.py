from django.conf import settings

from django.conf.urls.static import static

from .views import *

from django.urls import path

urlpatterns = [
        path("", Home, name="home"),
        path("post/<str:title>/", PostDetail, name="post")
        
    ]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
