from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # This shows the title and date in the list view
    list_display = ('title', 'created_at')
    # This adds a search bar
    search_fields = ('title', 'content')
