from django.urls import path

from django.conf.urls.static import static

from django.conf import settings

from .views import *

urlpatterns = [
        
        path("logins", Login_View, name="logins"),

        path("signup", SignUpView.as_view(), name="signup"),

        path("success", SuccessReg, name="success"),

        path("<int:uid>/<str:token>", ActivateView, name="activate"),
    ]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
