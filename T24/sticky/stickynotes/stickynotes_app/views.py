from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .forms import NoteForm
from .models import Note

def note_list(request):
    """view to display al notes.
    :param request: HTTP request object.
    :return: Rendered template with a list of notes
    """
    notes = Note.objects.filter(author=request.user)
    # creating a dictionary to pass data
    context = {
        "notes": notes, 
        "page_title": "list of notes",
    }
    return render(request, 'note_list.html', {'notes': notes})

def note_details(request, pk):
    """
    Display specific notes.
    :param request: HTTP request object.
    :param pk: Primary key of the post.
    :return: Rendered template with details of the specific note.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note':note})

def note_create(request):
    """
    View to create a new note.
    :param request: HTTP request object.
    :return: Rendered template for creating a new post.
    """
    if request.method == 'Note':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            if request.author.is_authenticated:
                note.author =request.author
            note.save
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/notes_form.html', {'form':form})

def note_update(request, pk):
    """ 
    View to update an existing note.
    :param request: HTTP request object.
    :param pk: Primary Key of the post to be updated.
    :return: Rendered template for updating the specified post
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'Note':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            post.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form':form})

def note_delete(request, pk):
    """
    view to delete a note.
    :param request: HTTP request object.
    :param pk: Primary Key of the post to be deleted.
    :return: Redirect to the note list after deletion"""
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect ('note_list')
        
    
# def index(request):
#     return render(request, 'stickynotes_app/index.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'stickynotes_app/register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f'You are now logged in as {username}.')
#                 return redirect('index')
#             else:
#                 messages.error(request, 'Invalid username or password.')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     form = AuthenticationForm()
#     return render(request, 'stickynotes_app/login.html', {'form': form})

# def logout_view(request):
#     logout(request)
#     messages.info(request, 'You have successfully logged out.')
#     return redirect('index')

# def protected_view(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     return render(request, 'stickynotes_app/protected.html')

