"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from hangarin_app.views import (
    HomePageView,
    CategoryList,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    TaskList,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    NoteList,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),

    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/new/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/new/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    path('notes/', NoteList.as_view(), name='note-list'),
    path('notes/new/', NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/edit/', NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]
