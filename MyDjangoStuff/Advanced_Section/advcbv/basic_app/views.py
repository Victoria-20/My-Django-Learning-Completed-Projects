from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponse
from basic_app import models

# Create your views here.
# --this is a functional view--
# def index(request):
#     return render(request, "index.html")


# --This is a class based view
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL")

# --This is aclass template view--
class IndexView(TemplateView):
    template_name = "index.html"


class SchoolListView(ListView):
    model = models.School
    context_object_name = "schools"


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = "basic_app/school_detail.html"


class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
