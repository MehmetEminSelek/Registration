from user.serializers import *
from Registration.serializers import *
from user.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .REG002PSWMNG import REG002PSWMNG


def REG009LOGIN(request):
    loginSerializer = LoginSerializer(data=request.data)
    err = errorCodes.error_codes
    if loginSerializer.is_valid() == False:
        return Response({"errId": 1, "errMessage": loginSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    if UserModel.objects.filter(user_Prog=loginSerializer.data["userProg"]).exists() == False:
        return Response({"errId": 30, "errMessage": err[29], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    loginSerializer.data["functionType"] = "V"
    REG002PSWMNG(loginSerializer.data)
