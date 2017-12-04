from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .models import VideoItem, SnippetItem
from .forms import VideoAddForm, SnippetAddForm

#-------------------------------------------------------------------------------

@login_required(login_url="/accounts/login")
def list_videos(request):
    if request.method == "POST":
        form = VideoAddForm(request.POST)
        if form.is_valid():
            video = form.save(commit = False);
            video.user_id = request.user;
            video.start = 0;
            video.end = 0;
            video.save();
            return redirect(list_videos)
    else:
        videos = VideoItem.objects.filter(user_id=request.user)
        form = VideoAddForm()
    return render(request, "list_videos.html", {'form':form, 'videos':videos})

#-------------------------------------------------------------------------------

def view_video(request, video_id, snippet_id = 0):
    video = get_object_or_404(VideoItem, pk=video_id)
    snippets = SnippetItem.objects.filter(video_id = video.id)
    if snippet_id == 0:
        form = SnippetAddForm(initial={'start': video.start, 'end': video.end})
    else:
        snippet = get_object_or_404(SnippetItem, pk=snippet_id)
        
        form = SnippetAddForm(initial={'title': snippet.title, 'start': snippet.start, 'end': snippet.end})
    return render(request, "view_video.html", {"video": video, "snippets": snippets, "form": form})
    
#-------------------------------------------------------------------------------

def add_snippet(request, video_id):
    video = get_object_or_404(VideoItem, pk=video_id);
    snippets = SnippetItem.objects.filter(video_id = video.id)
    
    form = SnippetAddForm(request.POST);
    if form.is_valid():
        snippet = form.save(commit = False);
        snippet.author = request.user
        snippet.video_id = video
        snippet.save()
        return redirect('view_video', video_id, snippet.id)

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

#-------------------------------------------------------------------------------