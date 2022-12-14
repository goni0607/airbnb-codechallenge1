from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.List.as_view(), name="list"),
    path("<int:pk>", views.Detail.as_view(), name="detail"),
    path("<int:pk>/edit", views.Update.as_view(), name="edit"),
    path("create", views.Create.as_view(), name="create"),
]
