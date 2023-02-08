from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from user.models import *
from user.serializers import CountryCodeSerializer, UserSerializer, UserAppSerializer
from datetime import datetime

from rest_framework import status

from datetime import datetime, timedelta

from .REG007SENDVERCODE import REG007SENDVERCODE

from .REG008CHECKVERCODE import REG008CHECKVERCODE
from .REG002PSWMNG import REG002PSWMNG

from .REG011IDCREATION import REG011IDCREATION
from .REG012CHKPROMO import REG012CHKPROMO

from Community.CMTY001 import PROCSAMECOUNTRY, PROCDIFFCOUNTRIES

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


community_base = "community"
#community_base = "community_test"


@api_view(['POST'])
def mainService(request):
    baseSerializer = BaseRequestSerializer(data=request)

    if baseSerializer.is_valid():
        if baseSerializer.data["callType"] == 1:
            return serviceOne(request)
        elif baseSerializer.data["callType"] == 2:
            return serviceTwo(request)
        elif baseSerializer.data["callType"] == 3:
            return serviceThree(request)
        elif baseSerializer.data["callType"] == 4:
            return serviceFour(request)
        elif baseSerializer.data["callType"] == 5:
            return serviceFive(request)
        elif baseSerializer.data["callType"] == 6:
            return serviceSix(request)
    else:
        return Response({"errId": errorCodes["errorCode"], "errMessage": errorCodes["description"]}, status=status.HTTP_400_BAD_REQUEST)


def serviceOne(request):
    serviceOneSerializer = ServiceOneSerializer(data=request.data)
    err = errorCodes.error_codes
    if serviceOneSerializer.is_valid() == False:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99, "err": serviceOneSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    if UserModel.objects.filter(user_Mail=serviceOneSerializer.data["userMail"]).exists():
        if serviceOneSerializer.data["userMail"] == UserModel.objects.get(user_Mail=serviceOneSerializer.data["userMail"]).user_Mail:
            dbModel = UserModel.objects.get(
                user_Mail=serviceOneSerializer.data["userMail"])
            if dbModel.user_Status > 4:
                return Response({"errId": 3, "errMessage": err[2], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
            elif dbModel.user_Status < 4:
                return Response({"errId": 4, "errMessage": err[3], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)

    # CHANGE AFTER THAT CAUSE WE DONT HAVE THAT YET BUT ITS GOING TO BE A DROPDOWN
    if CountryModel.objects.filter(country_coutrycode=serviceOneSerializer.data["userCountryCode"]).exists():
        return Response({"errId": 5, "errMessage": err[4], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)

    if UserModel.objects.filter(user_Prog=serviceOneSerializer.data["userPresenterID"]).exists():
        return Response({"errId": 6, "errMessage": err[5], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        UserModel.objects.create(
            user_Mail=serviceOneSerializer.data["userMail"],
            user_CountryCode=serviceOneSerializer.data["userCountryCode"],
            user_Language=serviceOneSerializer.data["userLanguage"],
            user_PresenterID=serviceOneSerializer.data["userPresenterID"],
            user_Type=serviceOneSerializer.data["userType"],
            user_phonePrefix=CountryModel.objects.using('community').get(
                country_coutrycode=serviceOneSerializer.data["userCountryCode"]).country_phoneprefix)
    except:
        return Response({"errId": 8, "errMessage": err[7], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)

    # -------------------------------------------------------------------------------------------------------------

    # CHECK USER_USERTYPE
    if serviceOneSerializer.data["userType"] == "CU":
        try:
            CustomerModel.objects.create(cus_progr=UserModel.objects.get(
                user_Mail=serviceOneSerializer.data["userMail"]).user_Prog)
        except:
            return Response({"errId": 8, "errMessage": err[7], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if serviceOneSerializer.data["userType"] == "CO":
        try:
            CompanyModel.objects.create(comp_prog=UserModel.objects.get(
                user_Mail=serviceOneSerializer.data["userMail"]).user_Prog,
                comp_mail=serviceOneSerializer.data["userMail"])
        except:
            return Response({"errId": 8, "errMessage": err[7], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if serviceOneSerializer.data["userType"] == "EX":
        try:
            ExpertModel.objects.create(comp_prog=UserModel.objects.get(
                exp_prog=serviceOneSerializer.data["userMail"]).user_Prog,
                exp_mail=serviceOneSerializer.data["userMail"])
        except:
            return Response({"errId": 8, "errMessage": err[7], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    serviceOneSerializer.data["userProg"] = UserModel.objects.get(
        user_Mail=serviceOneSerializer.data["userMail"]).user_Prog
    try:
        UserModel.objects.get(
            user_Mail=serviceOneSerializer.data["userMail"]).user_functionType = 'P'
    except:
        return Response({"errId": 8, "errMessage": err[7], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if REG007SENDVERCODE(serviceOneSerializer.data) == False:
        return Response({"errId": 8, "errMessage": err[7], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    output_user = UserModel.objects.get(
        user_Mail=serviceOneSerializer.data["userMail"])
    return Response({"errMessage": "Success", "RC": 0, "Output Data": {"Mail": output_user.user_Mail, "Country": output_user.user_CountryCode, "PresenterID": output_user.user_PresenterID, "Language": output_user.user_Language, "User Type": output_user.user_Type}}, status=status.HTTP_200_OK)


def serviceTwo(request):
    serviceTwoSerializer = ServiceTwoSerializer(data=request.data)
    err = errorCodes.error_codes
    if serviceTwoSerializer.is_valid() == False:
        return Response({"errId": 2, "errMessage": ServiceTwoSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    if UserModel.objects.filter(user_Prog=serviceTwoSerializer.data["userProg"]).exists() and UserModel.objects.get(
            user_Prog=serviceTwoSerializer.data["userProg"]).user_Prog != serviceTwoSerializer.data["userProg"]:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = UserModel.objects.get(
            user_Mail=serviceTwoSerializer.data["userMail"])
    except:
        return Response({"errId": 9, "errMessage": err[8], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if REG008CHECKVERCODE(serviceTwoSerializer.data) == False:
        return Response({"errId": 27, "errMessage": REG008CHECKVERCODE(serviceTwoSerializer.data).data["errMessage"], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user.user_Status = 2
        user.save()
    except:
        return Response({"errId": 10, "errMessage": err[9], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    output_ver = VerificationCodeModel.objects.get(
        verUserProg=serviceTwoSerializer.data["userProg"])
    output_user = UserModel.objects.get(
        user_Prog=serviceTwoSerializer.data["userProg"])
    return Response({"errMessage": "Success", "RC": 00, "Output Data": {"Prog": output_user.user_Prog, "Mail": output_user.user_Mail, "Verification Code": output_ver.verificationCode, "Function Type": output_user.user_functionType}}, status=status.HTTP_200_OK)


def serviceThree(request):
    serviceThreeSerializer = ServiceThreeSerializer(data=request.data)
    err = errorCodes.error_codes
    if serviceThreeSerializer.is_valid() == False:
        return Response({"errId": 1, "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        dbModel = UserModel.objects.get(
            user_Mail=serviceThreeSerializer.data["userMail"])
    except:
        return Response({"errId": 9, "errMessage": err[8], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if dbModel.user_Mail != serviceThreeSerializer.data["userMail"]:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        dbModel.user_Status = 3
        dbModel.user_mailStatus = "Y"
        dbModel.user_phoneNumber = serviceThreeSerializer.data["phoneNumber"]
        dbModel.user_phonePrefix = serviceThreeSerializer.data["phonePrefix"]
        dbModel.save()
    except:
        return Response({"errId": 10, "errMessage": err[9], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)

    if serviceThreeSerializer.data["userType"] == "CU":
        customer = CustomerModel.objects.get(
            cus_progr=serviceThreeSerializer.data["userProg"])
        try:
            customer.cus_name = serviceThreeSerializer.data["name"].upper()
            customer.cus_surname = serviceThreeSerializer.data["surname"].upper(
            )
            customer.cus_progr = serviceThreeSerializer.data["userProg"]
            customer.save()
        except:
            return Response({"errId": 8, "errMessage": err[7], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if serviceThreeSerializer.data["userType"] == "CO":
        company = CompanyModel.objects.get(
            comp_prog=serviceThreeSerializer.data["userProg"])  # USERPROG INSTEAD OF MAIL
        try:
            company.comp_prog = serviceThreeSerializer.data["userProg"]
            company.save()
        except:
            return Response({"errId": 8, "errMessage": err[7], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if serviceThreeSerializer.data["userType"] == "EX":
        expert = ExpertModel.objects.get(
            exp_mail=serviceThreeSerializer.data["userProg"])
        try:
            expert.exp_prog = serviceThreeSerializer.data["userProg"]
            expert.save()
        except:
            return Response({"errId": 8, "errMessage": err[7], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    SendVerCodeSerializer.userFunctionType = 'P'
    if REG007SENDVERCODE(serviceThreeSerializer.data) == False:
        return Response({"errId": 12, "errMessage": err[11], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    output_user = UserModel.objects.get(
        user_Prog=serviceThreeSerializer.data["userProg"])
    output_customer = CustomerModel.objects.get(
        cus_progr=serviceThreeSerializer.data["userProg"])
    return Response({"errorMessage": "Success", "RC": 00, "Output Data": {"Prog": output_user.user_Prog, "Mail": output_user.user_Mail, "Name": output_customer.cus_name, "Surname": output_customer.cus_surname, "Prefix": output_user.user_phonePrefix, "Phone Number": output_user.user_phoneNumber, "Function Type": output_user.user_functionType, "User Type": output_user.user_Type}}, status=status.HTTP_200_OK)


def serviceFour(request):
    serviceFourSerializer = ServiceFourSerializer(data=request.data)
    err = errorCodes.error_codes
    if serviceFourSerializer.is_valid() == False:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        dbModel = UserModel.objects.get(
            user_Mail=serviceFourSerializer.data["userMail"])
    except:
        return Response({"errId": 9, "errMessage": err[8], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if REG008CHECKVERCODE(serviceFourSerializer.data) == False:
        return Response({"errId": 27, "errMessage": err[26], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            dbModel.user_Status = 4
            dbModel.save()
        except:
            return Response({"errId": 10, "errMessage": err[9], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    output_user = UserModel.objects.get(
        user_Prog=serviceFourSerializer.data["userProg"])
    output_ver = VerificationCodeModel.objects.get(
        verUserProg=serviceFourSerializer.data["userProg"])
    return Response({"errorMessage": "Success", "Output Data": {"Prog": output_user.user_Prog, "Phone": output_user.user_phoneNumber, "Mail": output_user.user_Mail, "Function Type": output_user.user_functionType, "Verification Code": output_ver.verificationCode}}, status=status.HTTP_200_OK)


def serviceFive(request):
    serviceFiveSerializer = ServiceFiveSerializer(data=request.data)
    err = errorCodes.error_codes
    if serviceFiveSerializer.is_valid() == False:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        dbModel = UserModel.objects.get(
            user_Prog=serviceFiveSerializer.data["userProg"])
    except:
        return Response({"errId": 9, "errMessage": err[8], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    dbModel_app = UserApp.objects.get(
        appID=serviceFiveSerializer.data["appID"])
    if dbModel_app.appID != int(serviceFiveSerializer.data["appID"]):
        return Response({"errId": 13, "errMessage": err[12], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if REG002PSWMNG(serviceFiveSerializer.data) == False:
        return Response({"errId": 14, "errMessage": err[13], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        dbModel.user_Status = 5
        dbModel.user_username = serviceFiveSerializer.data["userName"]
        dbModel.user_acceptPrivacy = serviceFiveSerializer.data["regAcceptPrivacy"]
        dbModel.user_acceptTermsCondition = serviceFiveSerializer.data["regAcceptTermsCondition"]
        dbModel.user_acceptStatistics = serviceFiveSerializer.data["regAcceptStatistics"]
        dbModel.save()
    except:
        return Response({"errId": 10, "errMessage": err[9], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        dbModel_app.appID = serviceFiveSerializer.data["appID"]
        dbModel_app.userProg = serviceFiveSerializer.data["userProg"]
        dbModel_app.userStatus = 5
    except:
        return Response({"errId": 8, "errMessage": err[7], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    output_user = UserModel.objects.get(
        user_Prog=serviceFiveSerializer.data["userProg"])
    return Response({"errorMessage": "Success", "RC": 00, "Output Data": {"Prog": output_user.user_Prog, "Mail": output_user.user_Mail, "UserName": output_user.user_username, "AppID": dbModel_app.appID}}, status=status.HTTP_200_OK)


def serviceSix(request):
    serviceSixSerializer = ServiceSixSerializer(data=request.data)
    err = errorCodes.error_codes
    if serviceSixSerializer.is_valid() == False:
        return Response({"errId": 1,  "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    dbModel = UserModel.objects.get(
        user_Mail=serviceSixSerializer.data["userMail"])
    if REG012CHKPROMO(serviceSixSerializer.data).data["RC"] == 99:
        return Response({"errId": 26,  "errMessage": err[25], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if dbModel.user_Mail != serviceSixSerializer.data["userMail"]:
        return Response({"errId": 9,  "errMessage": err[8], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if REG011IDCREATION(serviceSixSerializer.data).data["RC"] == 99:
        return Response({"errId": 16, "errMessage": err[15], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        dbModel.user_promoCode = serviceSixSerializer.data["promoCode"]
        dbModel.user_userID = str(serviceSixSerializer.data["promoCode"])
        dbModel.save()
    except:
        return Response({"errId": 10,  "errMessage": err[9], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    output_user = UserModel.objects.get(
        user_Prog=serviceSixSerializer.data["userProg"])
    return Response({"errMessage": "Success", "Output Data": {"Prog": output_user.user_Prog, "Mail": output_user.user_Mail, "Language": output_user.user_Language}}, status=status.HTTP_200_OK)
