from django import forms
from .models import Books

class NewBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author']

class AssignOwnerForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['borrower']
        widgets = {'borrower': forms.HiddenInput()}

class RemoveOwner(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['borrower']
        widgets = {'borrower': forms.HiddenInput()}