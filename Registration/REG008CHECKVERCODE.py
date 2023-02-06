from user.serializers import *
from .serializers import *
from user.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta


def REG008CHECKVERCODE(userData):
    subService = REG008(data=userData)
    err = errorCodes.error_codes
    functionType = userData["userFunctionType"]
    if subService.is_valid():
        if functionType != ("M" or "P" or "W"):
            return False
    else:
        return False
    if UserModel.objects.filter(user_Prog=userData["userProg"]).exists() == False:
        return False
    if VerificationCodeModel.objects.filter(verUserProg=userData["userProg"]).exists() == False and VerificationCodeModel.objects.filter(verStartDate=datetime.now()).exists() == False:
        return False
    if VerificationCodeModel.objects.filter(verificationCode=userData["verificationCode"]).exists() == False:
        return False
    verification = VerificationCodeModel.objects.get(
        verificationCode=userData["verificationCode"])
    if verification.vercterr != 5 and verification.verstatus == "L":
        try:
            verification.verstatus = "L"
            verification.verlastLoginerr = datetime.now()
            verification.save()
            return False
        except:
            return False
    if datetime.now().minute < verification.verEndDate.minute:
        try:
            verification.verstatus = "E"
            verification.verlastLoginerr = datetime.now()
            verification.save()
            # return Response({"errId": 25, "errMessage": "GEN001ERR"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return False
    verification.verstatus = "A"
    if verification.verstatus == "E":
       return False
    if verification.verstatus == "L":
        return False
    if verification.verstatus == "A":
        try:
            verification.verlasttentative = datetime.now()
            verification.save()
        except:
            return False
