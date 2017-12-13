from django.conf.urls import url
from .views import list_videos, add_video, delete_video

urlpatterns = [
    url(r'^$', list_videos, name='list_videos'),
    url(r'^/(\d+)$', list_videos, name='list_videos'),
    url(r"^add$", add_video, name="add_video"),
    url(r"^add/(\d+)$", add_video, name="add_video"),
    # url(r"^edit/(\d+)$", edit_video, name="edit_video"),
    url(r"^delete/(\d+)$", delete_video, name="delete_video"),
    # url(r"^add/(\d+)/(\d+)$", add_snippet, name="add_snippet"),
    # url(r"^delete/(\d+)/(\d+)$", delete_snippet, name="delete_snippet"),
]
