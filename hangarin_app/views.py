from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from hangarin_app.models import Category, Task, Note

# Create your views here.

class HomePageView(ListView):
    model = Category
    context_object_name = 'home'
    template_name = "home.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stats"] = [
            {
                "label": "Categories",
                "count": Category.objects.count(),
                "icon": "la la-folder",
                "color": "bg-coquette-1",
            },
            {
                "label": "Tasks",
                "count": Task.objects.count(),
                "icon": "la la-tasks",
                "color": "bg-coquette-2",
            },
            {
                "label": "Completed",
                "count": Task.objects.filter(status="Completed").count(),
                "icon": "la la-check-circle",
                "color": "bg-coquette-3",
            },
            {
                "label": "Notes",
                "count": Note.objects.count(),
                "icon": "la la-sticky-note",
                "color": "bg-coquette-4",
            },
        ]
        return context
    
class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category_list.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs.update({'class': 'form-control'})
        return form


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs.update({'class': 'form-control'})
        return form


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category-list')
