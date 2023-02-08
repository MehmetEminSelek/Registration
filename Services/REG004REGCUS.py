from user.serializers import *
from .serializers import *
from user.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random
from datetime import datetime, timedelta


def REG004REGCUS(request):
    regCustomer = RegCustomerSerializer(data=request.data)
    err = errorCodes.error_codes
    if regCustomer.is_valid() == False:
        return Response({"errId": 1, "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if UserModel.objects.filter(userProg=regCustomer.data["userProg"]).exists() == False:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if UserModel.objects.filter(userProg=regCustomer.data["userProg"]).userType != "CU":
        return Response({"errId": 3, "errMessage": err[2], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if CustomerModel.objects.filter(customerUserProg=regCustomer.data["userProg"]).exists() == False:
        return Response({"errId": 4, "errMessage": err[3], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    user = UserModel.objects.get(userProg=regCustomer.data["userProg"])
    customer = CustomerModel.objects.get(
        cus_prog=regCustomer.data["userProg"])
    return Response(user, customer, status=status.HTTP_200_OK)
