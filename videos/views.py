from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re

from .models import VideoItem, SnippetItem
from .forms import VideoAddForm, SnippetAddForm

#-------------------------------------------------------------------------------

@login_required(login_url="/accounts/login")
def list_videos(request):
    videos = VideoItem.objects.filter(user = request.user)
    if request.method == "POST":
        form = VideoAddForm(request.POST)
        if form.is_valid():
            video = form.save(commit = False);
            yt_id = getYouTubeId(video.url)
            if yt_id != -1:
                video.url = yt_id;
                video.user = request.user;
                video.start = 0;
                video.end = 0;
                video.save();
                return redirect(list_videos)
            else:
                messages.success(request, "Not a valid YouTube URL", extra_tags='danger') 
        else:
            messages.success(request, "Not a valid YouTube URL", extra_tags='danger')     
    else:
        form = VideoAddForm()
    return render(request, "list_videos.html", {'form':form, 'videos':videos})

#-------------------------------------------------------------------------------

def view_video(request, video_id, snippet_id = '0'):
    video = get_object_or_404(VideoItem, pk=video_id)
    yt_id = video.url;
    snippets = SnippetItem.objects.filter(video_id = video.id)
    if snippet_id == '0':
        snippet = SnippetItem()
        snippet.id = 0
        form = SnippetAddForm(initial={'snippet': snippet, 'title':'', 'start': video.start, 'end': video.end, 'jump': '0'})
    else:
        snippet = get_object_or_404(SnippetItem, pk=snippet_id)
        form = SnippetAddForm(initial={'title': snippet.title, 'start': snippet.start, 'end': snippet.end, 'jump': snippet.jump})
    return render(request, "view_video.html", {"video": video, 'yt_id': yt_id, 'snippet':snippet, "snippets": snippets, "form": form})
    
#-------------------------------------------------------------------------------

def add_snippet(request, video_id, snippet_id ):
    print(snippet_id)
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

def getYouTubeId(url):
    url1 = url.split("v=", 1)
    if len(url1) == 1:
        return -1
    else:
        url2 = url1[1].split("?",1)
        url3 = url2[0].split("&",1)
        yt_id = str(url3[0])
        return  yt_id

#-------------------------------------------------------------------------------

# def update_snippet(request, video_id):
#     pass
    # video = get_object_or_404(VideoItem, pk=video_id);
    # snippets = SnippetItem.objects.filter(video_id = video.id)
    
    # form = SnippetAddForm(request.POST);
    # if form.is_valid():
    #     snippet = form.save(commit = False);
    #     snippet.author = request.user
    #     snippet.video_id = video
        # if snippet.title in [s.title for s in snippets]:
        #     print("snippet exists")
        #     s = SnippetItem.objects.filter(video_id = video.id, title = snippet.title)
        #     form = SnippetAddForm(request.POST, instance = s);
        #     print(s.video_id)
        # else:
        # snippet.save()
        # return redirect('view_video', video_id, snippet.id)


#------------------------------------------------------------------------------