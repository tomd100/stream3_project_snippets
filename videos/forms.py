from django import forms
from .models import VideoItem, SnippetItem

#-------------------------------------------------------------------------------

class VideoAddForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Video Title',
        widget = forms.TextInput(
            attrs = {'class': 'field_input'}
        )
    )
    url = forms.CharField(
        label = 'Video Url',
        widget = forms.TextInput(
            attrs = {'class': 'field_input'}
        )
    )        
    class Meta:
        model = VideoItem
        fields = ['title', 'url']


#-------------------------------------------------------------------------------

class SnippetAddForm(forms.ModelForm):
    title = forms.CharField(
        widget = forms.TextInput(
            attrs = {'class': 'snippet_title'}
        )
    );
    start = forms.CharField(
        widget = forms.TextInput(
            attrs = {'class': 'snippet_markers'}
        )
    );
    end = forms.CharField(
        widget = forms.TextInput(
            attrs = {'class': 'snippet_markers'}
        )
    );
    class Meta:
        model = SnippetItem
        fields = ['title', 'start', 'end']
        
#-------------------------------------------------------------------------------

# form = JournalForm(initial={'tank': 123})
# or set the value in the form definition:

# tank = forms.IntegerField(widget=forms.HiddenInput(), initial=123) 