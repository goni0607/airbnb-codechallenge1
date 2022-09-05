from django.urls import path
from . import views as core_views

app_name = "core"

urlpatterns = [
    path("", core_views.home, name="home"),
    path("search/", core_views.search, name="search"),
    path("genres/<str:genre>/", core_views.genres, name="genres"),
]
