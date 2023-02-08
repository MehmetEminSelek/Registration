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


def REG004REGCUSBDATE(request):
    regCustomerBdateSerializer = RegCustomerBdateSerializer(
        data=request.data)
    err = errorCodes.error_codes
    if regCustomerBdateSerializer.is_valid() == False:
        return Response({"errId": 1, "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if CustomerModel.objects.filter(cus_prog=regCustomerBdateSerializer.data["userProg"]).exists() == False:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    customer = CustomerModel.objects.get(
        cus_prog=regCustomerBdateSerializer.data["userProg"])
    try:
        customer.cus_birthdate = regCustomerBdateSerializer.data["bdate"]
        customer.save()
    except:
        return Response({"errId": 3, "errMessage": err[2], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
