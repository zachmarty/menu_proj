from django.urls import path
from menu.views import *
from menu.apps import MenuConfig

app_name = MenuConfig.name

urlpatterns = [
    path("", MenuListView.as_view(), name="index"),
    path("<slug:slug>", MenuDetailView.as_view(), name="view"),
    path("delete/<slug:slug>", MenuDeleteView.as_view(), name="delete"),
]
