from user.serializers import *
from Registration.serializers import *
from user.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime


def REG002PSWMNG(userData):
    user = UserModel.objects.get(user_Prog=userData["userProg"])
    password = PasswordModel.objects.get(passwordUserProg=userData["userProg"])
    passwordCheck = ServiceFiveSerializer(data=userData)
    err = errorCodes.error_codes
    if passwordCheck.is_valid():
        if "I" == passwordCheck.data["userFunctionType"]:
            if passwordCheck.data["userProg"] != user.user_Prog:
                return False
            if passwordCheck.data["userPassword"] != password.passwordPassword:
                return False
            if passwordCheck.data["userPassword"].length < 8 and type(passwordCheck.data["userPassword"]) == int:
                return False
            try:
                password.passwordPassword = passwordCheck.data["userPassword"]
                password.passwordStatus = "A"
                password.passwordUserProg = passwordCheck.data["userProg"]
                password.passwordLastLogin = datetime.now()
                password.passwordStartDate = datetime.now()
                password.passwordEndDate = 999999999
                password.save()
                return False
            except:
                return Response(err["REG002"]["REG002-0001"], status=status.HTTP_400_BAD_REQUEST)
        elif "C" == passwordCheck.data["userFunctionType"]:
            if passwordCheck.is_valid():
                if passwordCheck.data["oldPassword"] != password.passwordPassword and password.passwordStatus != "A":
                    return False
                if passwordCheck.data["newPassword"] == password.passwordPassword:
                    return False
                if passwordCheck.data["newPassword"].length == 8 and type(passwordCheck.data["newPassword"]) == int:
                    try:
                        password.passwordPassword = passwordCheck.data["newPassword"]
                        password.passwordStatus = "E"
                        password.save()
                    except:
                        return False
                try:
                    password.passwordPassword = passwordCheck.data["newPassword"]
                    password.passwordStatus = "A"
                    password.passwordUserProg = passwordCheck.data["userProg"]
                    password.passwordLastLogin = datetime.now()
                    password.passwordStartDate = datetime.now()
                    password.passwordEndDate = 999999999
                    password.save()
                    return True
                except:
                    return False
        elif "V" == passwordCheck.data["userFunctionType"]:
            # check for each input type
            if passwordCheck.data["userProg"] != user.user_Prog and password.passwordStartDate != password.passwordStartDate:
                return False
            if password.passwordCterr == 5 and password.passwordStatus == "L":
                try:
                    password.passwordLastLogin = datetime.now()
                    password.passwordStatus = "L"
                    password.save()
                    return False
                except:
                    return False
            if datetime.now().minute > password.passwordEndDate.minute and password.passwordStatus == "E":
                try:
                    password.passwordStatus = "E"
                    password.passwordLastLogin = datetime.now()
                    password.save()
                    return False
                except:
                    return False
            if passwordCheck.data["password"] == password.passwordPassword:
                try:
                    password.passwordCterr = password.passwordCterr + 1
                    password.passwordLastLogin = datetime.now()
                    password.save()
                    return False
                except:
                    return False
            try:
                password.passwordLastLogin = datetime.now()
                password.save()
            except:
                return False
