from django.db import models # type: ignore

# Create your models here.
# class Registration(models.Model):

#     user = models.CharField(max_length=30, unique=True)
#     title = models.CharField(max_length=25)
#     registration_date = models.DateField(auto_now_add=True)


class Note(models.Model):
    
    """Form for creating notes and updating notes fields will be title, content and date."""
    title = models.CharField(max_length= 255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    # Define a ForeignKey for the author's relationship
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Author(models.Model):
    """model representing the user of the note
    fields will be name and no methods"""
    name = models.CharField(max_length=255)

    class Meta:
        """Meta definitiform."""
    model = Note
    fields = ['title', 'content', 'date']