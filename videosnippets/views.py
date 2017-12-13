from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re

from videos.models import VideoItem
from .models import SnippetItem
from .forms import SnippetAddForm

#-------------------------------------------------------------------------------

def view_video(request, video_id, snippet_id = '0'):
    video = get_object_or_404(VideoItem, pk=video_id)
    yt_id = video.yt_id;
    snippets = SnippetItem.objects.filter(video_id = video.id)
    if snippet_id == '0':
        snippet = SnippetItem()
        snippet.id = 0
        form = SnippetAddForm(initial={'snippet': snippet, 'title':'', 'start': video.start, 'end': video.end, 'jump': '2'})
    else:
        snippet = get_object_or_404(SnippetItem, pk=snippet_id)
        form = SnippetAddForm(initial={'title': snippet.title, 'start': snippet.start, 'end': snippet.end, 'jump': snippet.jump})
    return render(request, "view_video.html", {"video": video, 'yt_id': yt_id, 'snippet':snippet, "snippets": snippets, "form": form})
    
#-------------------------------------------------------------------------------

def add_snippet(request, video_id, snippet_id ):
    video = get_object_or_404(VideoItem, pk = video_id);
    snippets = SnippetItem.objects.filter(video = video)
    if snippet_id == '0':
        form = SnippetAddForm(request.POST);
        if form.is_valid():
            snippet = form.save(commit = False);
            snippet.video = video
            snippet.save()
    else:
        snippet = get_object_or_404(SnippetItem, pk=snippet_id);
        form = SnippetAddForm(request.POST, instance = snippet);
        if form.is_valid():
            form.save()
    return redirect('view_video', video_id, snippet_id)

#-------------------------------------------------------------------------------

def delete_snippet(request, video_id, snippet_id ):
    snippet = SnippetItem.objects.filter(pk = snippet_id)
    SnippetItem.objects.filter(pk=snippet_id).delete();
    snippet_id = 0
    return redirect('view_video', video_id, snippet_id) 

#-------------------------------------------------------------------------------
