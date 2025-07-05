from django.contrib import admin
from django.urls import path
from .views import (
    Basepageview,
    Blogdetailview,
    Blogcreateview,
    Detailyangilash,
    Postdelete,
)


urlpatterns = [
    path("", Basepageview.as_view(), name="home"),
    path("post/<int:pk>/", Blogdetailview.as_view(), name="detail_view"),
    path("post/new", Blogcreateview.as_view(), name="detail_new"),
    path("post/<int:pk>/edit", Detailyangilash.as_view(), name="detail_yangilash"),
    path("post/<int:pk>/delete/", Postdelete.as_view(), name="post_delete"),
]
