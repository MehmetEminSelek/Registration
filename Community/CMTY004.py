from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from Registration.serializers import *
from user.models import *
from user.serializers import CountryCodeSerializer, UserSerializer, UserAppSerializer
from datetime import datetime


def CMTY004(request):
    RewardPointsManagementSerializer = RewardPointsManagementSerializer(
        data=request.data)
    err = errorCodes.error_codes
    if RewardPointsManagementSerializer.is_valid() == False:
        return Response({"errId": 1, "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if RewardPointsManagementSerializer.data["usercountry"] != "":
        if UserModel.objects.get(userCountry=RewardPointsManagementSerializer.data["user_countrycode"]).user_Prog == RewardPointsManagementSerializer.data["user_countrycode"]:
            return Response({"errId": 33, "errMessage": err[32], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        input_userCountry = UserModel.objects.get(
            user_Prog=RewardPointsManagementSerializer.data["userProg"])
        user_CountryCode = input_userCountry.user_CountryCode
    except:
        return Response({"errId": 33, "errMessage": err[32], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)

# Continue CMTY RC=00 statement & PROCESS
