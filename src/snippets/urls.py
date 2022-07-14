from django.urls import re_path

from snippets.views import snippet_list, snippet_detail


urlpatterns = [
    re_path(r'^snippets/$', snippet_list),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail),
]