from user.serializers import *
from .serializers import *
from user.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random
from datetime import datetime, timedelta
from .REG007SENDVERCODE import REG007SENDVERCODE
from .REG008CHECKVERCODE import REG008CHECKVERCODE
from .REG004REGCUS import REG004REGCUS
from .REG004REGCUSBDATE import REG004REGCUSBDATE
from .REG004REGCUSNAME import REG004REGCUSNAME
from .REG004REGCUSSUR import REG004REGCUSSUR



@api_view(['POST'])
def REG004PHONEVERIFY(request):
    if request.data["phone_callType"] == 1:
        phoneSerializer = PhoneSerializer(data=request.data)
        err = errorCodes.error_codes
        if phoneSerializer.is_valid() == False:
            return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
        if UserModel.objects.filter(userProg=phoneSerializer.data["phone_userProg"]).exists() == False:
            return Response({"errId": 3, "errMessage": err[2], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
        userProg = UserModel.objects.get(
            user_Prog=phoneSerializer.data["phone_userProg"]).user_Prog
        try:
            ChangePhone.objects.create(
                phone_userProg=userProg,
                phone_number=phoneSerializer.data["phone_phone"],
                phone_status=1,
                phone_endverification=datetime.now() + timedelta(minutes=5))
        except:
            return Response({"errId": 10, "errMessage": err[9], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
        if REG007SENDVERCODE(phoneSerializer.data) == True:
            return Response({"errId": 0, "RC": 00}, status=status.HTTP_200_OK)
        else:
            return Response({"errId": 1, "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if request.data["phone_callType"] == 2:
        phoneSerializerVerify = PhoneSerializerVerify(data=request.data)
        if phoneSerializerVerify.is_valid() == False:
            return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
        if UserModel.objects.filter(userProg=phoneSerializerVerify.data["phone_userProg"]).exists() == False:
            return Response({"errId": 3, "errMessage": err[2], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
        if REG008CHECKVERCODE(phoneSerializerVerify.data) == False:
            return Response({"errId": 4, "errMessage": err[3], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
        changePhone = ChangePhone.objects.get(
            userProg=phoneSerializerVerify.data["phone_userProg"])
        user = UserModel.objects.get(user_Prog=changePhone.phone_userprogr)
        try:
            changePhone.phone_status = 2
            changePhone.phone_number = user.user_phoneNumber
            changePhone.phone_endvalidity = datetime.now()
            changePhone.phone_endverification = "0000-00-00 00:00:00"
        except:
            return Response({"errId": 10, "errMessage": err[9], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user.user_phoneNumber = phoneSerializerVerify.data["phone_userPhone"]
            user.save()
        except:
            return Response({"errId": 10, "errMessage": err[9], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)


# def REG004REGCUS(request):
#     regCustomer = RegCustomerSerializer(data=request.data)
#     err = errorCodes.error_codes
#     if regCustomer.is_valid() == False:
#         return Response({"errId": 1, "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
#     if UserModel.objects.filter(userProg=regCustomer.data["userProg"]).exists() == False:
#         return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
#     if UserModel.objects.filter(userProg=regCustomer.data["userProg"]).userType != "CU":
#         return Response({"errId": 3, "errMessage": err[2], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
#     if CustomerModel.objects.filter(customerUserProg=regCustomer.data["userProg"]).exists() == False:
#         return Response({"errId": 4, "errMessage": err[3], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
#     user = UserModel.objects.get(userProg=regCustomer.data["userProg"])
#     customer = CustomerModel.objects.get(
#         cus_prog=regCustomer.data["userProg"])
#     return Response(user, customer, status=status.HTTP_200_OK)


# def REG004REGCUSSUR(request):
#     regCustomerSurnameSerializer = RegCustomerSurnameSerializer(
#         data=request.data)
#     err = errorCodes.error_codes
#     if regCustomerSurnameSerializer.is_valid() == False:
#         return Response({"errId": 1, "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
#     if CustomerModel.objects.filter(cus_prog=regCustomerSurnameSerializer.data["userProg"]).exists() == False:
#         return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
#     customer = CustomerModel.objects.get(
#         cus_prog=regCustomerSurnameSerializer.data["userProg"])
#     try:
#         customer.cus_surname = regCustomerSurnameSerializer.data["cus_surname"]
#         customer.save()
#     except:
#         return Response({"errId": 3, "errMessage": err[2], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)


# def REG004REGCUSNAME(request):
#     regCustomerNameSerializer = RegCustomerNameSerializer(data=request.data)
#     err = errorCodes.error_codes
#     if regCustomerNameSerializer.is_valid() == False:
#         return Response({"errId": 1, "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
#     if CustomerModel.objects.filter(cus_prog=regCustomerNameSerializer.data["userProg"]).exists() == False:
#         return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
#     customer = CustomerModel.objects.get(
#         cus_prog=regCustomerNameSerializer.data["userProg"])
#     try:
#         customer.cus_name = regCustomerNameSerializer.data["cus_name"]
#         customer.save()
#     except:
#         return Response({"errId": 3, "errMessage": err[2], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)


# def REG004REGCUSBDATE(request):
#     regCustomerBdateSerializer = RegCustomerBdateSerializer(
#         data=request.data)
#     err = errorCodes.error_codes
#     if regCustomerBdateSerializer.is_valid() == False:
#         return Response({"errId": 1, "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
#     if CustomerModel.objects.filter(cus_prog=regCustomerBdateSerializer.data["userProg"]).exists() == False:
#         return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
#     customer = CustomerModel.objects.get(
#         cus_prog=regCustomerBdateSerializer.data["userProg"])
#     try:
#         customer.cus_birthdate = regCustomerBdateSerializer.data["bdate"]
#         customer.save()
#     except:
#         return Response({"errId": 3, "errMessage": err[2], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
