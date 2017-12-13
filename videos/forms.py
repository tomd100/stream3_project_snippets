from django import forms
from .models import VideoItem

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

# form = JournalForm(initial={'tank': 123})
# or set the value in the form definition:

# tank = forms.IntegerField(widget=forms.HiddenInput(), initial=123) 