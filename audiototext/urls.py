from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import index, upload_file


urlpatterns = [
    path("", index, name="index"),
    path('upload/', upload_file, name="upload"),
    path('accounts/', include('django.contrib.auth.urls'))
]