from django.urls import path
from rest_framework.routers import DefaultRouter

from follows.views.followers_list_view import FollowersListView
from follows.views.following_list_view import FollowingListView

router = DefaultRouter()

urlpatterns = [
    path(
        "<int:user_id>/followers/",
        FollowersListView.as_view(),
        name="followers-list",
    ),
    path(
        "<int:user_id>/following/",
        FollowingListView.as_view(),
        name="following-list",
    ),
]

urlpatterns += router.urls
