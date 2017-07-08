from django.conf.urls import url
from .views import (
    view_todos,
    get_todo
)


urlpatterns = [
    url(r'^view_todos/$', view_todos),
    url(r'^get_todo/(?P<todo_id>[0-9a-z-]+)/$', get_todo),
]
