from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from user.models import User
from user.serializers.register_serializer import UserRegisterSerializer


class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]