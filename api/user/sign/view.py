from rest_framework.views import APIView
from common.library import *


class SignAPI(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        return APIResponse(STATUS_SUCCESS)
