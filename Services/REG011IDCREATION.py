from user.serializers import *
from Registration.serializers import *
from user.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random
from datetime import datetime, timedelta


# dont need to do with service do on code
def REG011IDCREATION(userData):
    dbModel = UserModel.objects.get(user_Prog=userData["userProg"])
    dbModel.user_userID = dbModel.user_CountryCode + str(userData["userProg"])

    return dbModel.user_userID
