from django.urls import path
from .views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('new/', NoteCreateView.as_view(), name='note_create'),
    path('edit/<int:pk>/', NoteUpdateView.as_view(), name='note_update'),
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='note_delete'),
]
