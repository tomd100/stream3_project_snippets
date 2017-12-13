from django.conf.urls import url
from .views import view_video, add_snippet, delete_snippet

urlpatterns = [
    url(r"^(\d+)$", view_video, name="view_video"),
    url(r"^(\d+)/(\d+)$", view_video, name="view_video"),
    url(r"^add/(\d+)/(\d+)$", add_snippet, name="add_snippet"),
    url(r"^delete/(\d+)/(\d+)$", delete_snippet, name="delete_snippet"),
]
