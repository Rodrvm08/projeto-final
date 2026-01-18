from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views.me_views import MeView
from users.views.popular_user_viewset import PopularUsersViewSet
from users.views.user_register_viewset import UserRegisterViewSet
from users.views.user_viewset import UserViewSet

router = DefaultRouter()
router.register("all-users", UserViewSet, basename="users")
router.register("popular-users", PopularUsersViewSet, basename="popular-users")

urlpatterns = [
    path("me/", MeView.as_view(), name="users-me"),
    path("register/", UserRegisterViewSet.as_view({"post": "create"})),
]

urlpatterns += router.urls