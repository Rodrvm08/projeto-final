
from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.views.post_view_set import PostViewSet
from posts.views.user_posts_view import UserPostsView


router = DefaultRouter()
router.register("", PostViewSet, basename="posts")


urlpatterns = [

    path(
        "user/<str:username>/",
        UserPostsView.as_view(),
        name="posts-by-user",
    ),
]

urlpatterns += router.urls