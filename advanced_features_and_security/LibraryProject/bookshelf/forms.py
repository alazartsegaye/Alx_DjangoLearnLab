from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    # Custom validation for the title field
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

    # Custom validation for the author field
    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author.replace(" ", "").isalpha():  # Ensure only letters
            raise forms.ValidationError("Author name should contain only letters.")
        return author

    # Custom validation for publication year
    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year < 1500 or year > 2100:
            raise forms.ValidationError("Publication year must be between 1500 and 2100.")
        return year

