from django.conf.urls import url
from .views import list_videos, view_video, add_snippet

urlpatterns = [
    url(r'^list$', list_videos, name='list_videos'),
    url(r"^view/(\d+)$", view_video, name="view_video"),
    url(r"^view/(\d+)/(\d+)$", view_video, name="view_video"),
    url(r"^snippet/(\d+)$", add_snippet, name="add_snippet"),
]
