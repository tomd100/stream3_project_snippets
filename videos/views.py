from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re

from .models import VideoItem
from .forms import VideoAddForm

#-------------------------------------------------------------------------------

def list_videos(request, video_id = '0'):
    videos = VideoItem.objects.filter(user = request.user)
    if video_id == '0':
        video = VideoItem()
        video.id = 0
        # form = VideoAddForm(initial={'video': video, 'title':'', 'url': ''})
        form = VideoAddForm()
    else:
        video = get_object_or_404(VideoItem, pk=video_id)
        form = VideoAddForm(initial={'title': video.title, 'url': video.url})
    return render(request, "list_videos.html", {'videos':videos, 'video': video, 'form':form})

#-------------------------------------------------------------------------------

@login_required(login_url="/accounts/login")
def add_video(request, video_id = '0'):
    if video_id == '0':
        form = VideoAddForm(request.POST)
        if form.is_valid():
            video = form.save(commit = False);
            yt_id = getYouTubeId(video.url)
            if yt_id != -1:
                video.yt_id = yt_id;
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
        video = get_object_or_404(VideoItem, pk=video_id);
        form = VideoAddForm(request.POST, instance = video);
        if form.is_valid():
            form.save()
    return redirect(list_videos)

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

def delete_video(request, video_id):
    VideoItem.objects.filter(pk=video_id).delete();
    video_id = 0
    return redirect(list_videos) 

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