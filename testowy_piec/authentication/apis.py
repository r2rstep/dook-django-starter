from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from testowy_piec.api.mixins import ApiAuthMixin

from testowy_piec.users.selectors import user_get_login_data


class UserLoginApi(TokenObtainPairView):
    pass


class UserMeApi(ApiAuthMixin, APIView):
    def get(self, request):
        data = user_get_login_data(user=request.user)

        return Response(data)
