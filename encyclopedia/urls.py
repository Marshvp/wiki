from django.urls import path
from .views import content_page

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/wiki/<str:title>/", views.entry_detail, name='entry_detail'),
    path('content/<str:filename>/', content_page, name='content_page'),
]
