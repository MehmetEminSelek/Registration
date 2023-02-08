from user.serializers import *
from .serializers import *
from user.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random
from datetime import datetime, timedelta


def REG007SENDVERCODE(request):
    user = UserModel.objects.get(user_Mail=request["userMail"])
    err = errorCodes.error_codes
    if UserModel.objects.filter(user_Mail=request["userMail"]).exists() == False:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if VerificationCodeModel.objects.filter(verUserProg=user.user_Prog).exists() == True:
        ver = VerificationCodeModel.objects.get(
            verUserProg=user.user_Prog)
        ver.verstatus = "A"
        ver.save()
        return Response({"errId": 1, "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    verification_code = random.randrange(10000, 99999)
    try:
        VerificationCodeModel.objects.create(
            verUserProg=user.user_Prog,
            verificationCode=verification_code,
            verStartDate=datetime.now(),
            verstatus="A",
            verCodeType="V",
            verEndDate=datetime.now() + timedelta(minutes=5))
    except:
        return False
