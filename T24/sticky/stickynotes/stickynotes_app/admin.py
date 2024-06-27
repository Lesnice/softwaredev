# Register your models here.
from django.contrib import admin
from .models import Note
from .models import Author

# new note
admin.site.register(Note)
#Author model
admin.site.register(Author)

# @admin.register(Note)
# class NoteAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'created_at')
#     search_fields = ('title', 'author__username')  # Assuming author is a ForeignKey to User model