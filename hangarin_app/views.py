from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from hangarin_app.models import Category, Task, Note, Priority

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


class NoteList(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().select_related('task')
        query = self.request.GET.get('q')
        created = self.request.GET.get('created')
        if query:
            queryset = queryset.filter(content__icontains=query)
        if created:
            queryset = queryset.filter(created_at__date=created)
        return queryset.order_by('-created_at')


class NoteCreateView(CreateView):
    model = Note
    fields = ['task', 'content']
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['task'].widget.attrs.update({'class': 'form-control'})
        form.fields['content'].widget.attrs.update({'class': 'form-control', 'rows': 4})
        return form


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['task', 'content']
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['task'].widget.attrs.update({'class': 'form-control'})
        form.fields['content'].widget.attrs.update({'class': 'form-control', 'rows': 4})
        return form


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('note-list')


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().select_related('category', 'priority')
        query = self.request.GET.get('q')
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        category = self.request.GET.get('category')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )

        if status:
            queryset = queryset.filter(status=status)

        if priority:
            queryset = queryset.filter(priority_id=priority)

        if category:
            queryset = queryset.filter(category_id=category)

        return queryset.order_by('-deadline')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Task.STATUS_CHOICES
        context['priorities'] = Priority.objects.all()
        context['categories'] = Category.objects.all()
        return context


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status', 'priority', 'category']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['title'].widget.attrs.update({'class': 'form-control'})
        form.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 4})
        form.fields['deadline'].widget.attrs.update({'class': 'form-control'})
        form.fields['status'].widget.attrs.update({'class': 'form-control'})
        form.fields['priority'].widget.attrs.update({'class': 'form-control'})
        form.fields['category'].widget.attrs.update({'class': 'form-control'})
        return form


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status', 'priority', 'category']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['title'].widget.attrs.update({'class': 'form-control'})
        form.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 4})
        form.fields['deadline'].widget.attrs.update({'class': 'form-control'})
        form.fields['status'].widget.attrs.update({'class': 'form-control'})
        form.fields['priority'].widget.attrs.update({'class': 'form-control'})
        form.fields['category'].widget.attrs.update({'class': 'form-control'})
        return form


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
