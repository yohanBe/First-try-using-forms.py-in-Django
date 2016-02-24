from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/',
        views.blogpostcreateviews.as_view(),
        name='blog_post_create'),
]
