from user.serializers import *
from Registration.serializers import *
from user.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random
from datetime import datetime, timedelta


def REG012CHKPROMO(userData):
    return Response({"errMessage": "Success", "RC": 0}, status=status.HTTP_200_OK)
