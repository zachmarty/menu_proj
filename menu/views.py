from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from menu.models import Menu


class MenuListView(ListView):
    model = Menu

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(parent__isnull=True)
        return queryset


class MenuDetailView(DetailView):
    model = Menu

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        menu = self.object
        parent = menu.parent
        if parent == None:
            siblings = Menu.objects.filter(parent__isnull=True)
        else:
            siblings = Menu.objects.filter(parent=parent.id)
        context_data["siblings"] = siblings
        childs = Menu.objects.filter(parent=menu)
        context_data["childs"] = childs
        return context_data


class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy("menu:index")
