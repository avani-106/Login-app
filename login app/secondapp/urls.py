from django.urls import path
from . import views
# 
# for file uploading
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('',views.direct),
    path('upload',views.upload)
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    