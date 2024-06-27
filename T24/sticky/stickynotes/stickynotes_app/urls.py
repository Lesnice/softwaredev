# stickynotes_app/urls.py

from django.urls import path # type: ignore
from .views import note_list, note_details, note_create, note_update, note_delete # type: ignore
# from .views import register, login_view, logout_view, protected_view
# from . import views

urlpatterns = [
    path('', note_list, name='note_list'),
    path('stickynotes_app/<int:pk>/', note_details, name='note_detail'),
    path('stickynotes_app/new/', note_create, name='note_create'),
    path('stickynotes_app/<int:pk>edit/', note_update, name='note_update'),
    path('stickynotes_app/<int:pk>/delete/', note_delete, name='note_delete'),
    ]