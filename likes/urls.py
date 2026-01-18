from django.urls import path

from likes.views.like_toggle_view import LikeToggleView
from likes.views.post_likes_list_view import PostLikesListView

urlpatterns = [

    path(
        "posts/<int:post_id>/",
        LikeToggleView.as_view(),
        name="like-toggle",
    ),

    path(
        "posts/<int:post_id>/users/",
        PostLikesListView.as_view(),
        name="post-likes-list",
    ),
]