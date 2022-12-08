from django.urls import path
from . import views

urlpatterns = [
    path("videos", views.getVideo),
    path("files", views.getFile)
]
