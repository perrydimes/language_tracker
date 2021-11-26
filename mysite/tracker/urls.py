from django.urls import path

from . import views

urlpatterns = [
    # ex: /tracker/
    path('', views.index, name='index'),
    path('entry/new/', views.entry, name='entry_new'),
    path('entry/edit/<int:entry_id>/', views.entry, name='entry_edit'),
]
