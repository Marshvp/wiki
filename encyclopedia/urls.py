from django.urls import path
from .views import content_page, entry_detail, index, search_results, new_page

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search/", search_results, name='search_results'),
    path("wiki/create/", new_page, name='new_page'),
    path("wiki/<str:title>/", entry_detail, name='entry_detail'),
    path('wiki/<str:filename>/', content_page, name='content_page'),
    path("wiki/", views.index, name="index")
]
