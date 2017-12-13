from django import forms
from .models import SnippetItem
from videos.models import VideoItem

#-------------------------------------------------------------------------------

class SnippetAddForm(forms.ModelForm):
    title = forms.CharField(
        widget = forms.TextInput(
            attrs = {'class': 'snippet_title'}
        )
    );
    start = forms.CharField(
        widget = forms.TextInput(
            attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}
        )
    );
    end = forms.CharField(
        widget = forms.TextInput(
            attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}
        )
    );
    jump = forms.CharField(
        widget = forms.TextInput(
            attrs = {'class': 'snippet_markers', 'type':'number', 'step':'0.1'}
        )
    );
    class Meta:
        model = SnippetItem
        fields = ['title', 'start', 'end', 'jump']
        