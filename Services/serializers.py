from rest_framework import serializers
from django.core.exceptions import ValidationError


class BaseRequestSerializer(serializers.Serializer):
    callType = serializers.IntegerField(min_value=1, max_value=6)


class ServiceOneSerializer(serializers.Serializer):
    callType = serializers.IntegerField(min_value=1, max_value=6)
    userMail = serializers.CharField(max_length=50)
    userCountryCode = serializers.CharField(max_length=2)
    userLanguage = serializers.CharField(max_length=2)
    userPresenterID = serializers.IntegerField()
    userType = serializers.CharField(max_length=2)


class ServiceTwoSerializer(serializers.Serializer):
    callType = serializers.IntegerField(min_value=1, max_value=6)
    userProg = serializers.IntegerField()
    userMail = serializers.CharField(max_length=50)
    verificationCode = serializers.CharField(max_length=16)
    userFunctionType = serializers.CharField(max_length=1)


class ServiceThreeSerializer(serializers.Serializer):
    callType = serializers.IntegerField(min_value=1, max_value=6)
    userProg = serializers.IntegerField()
    userMail = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=30)
    surname = serializers.CharField(max_length=30)
    phonePrefix = serializers.CharField(max_length=7)
    phoneNumber = serializers.DecimalField(max_digits=20, decimal_places=2)
    userFunctionType = serializers.CharField(max_length=1)
    userType = serializers.CharField(max_length=2)


class ServiceFourSerializer(serializers.Serializer):
    callType = serializers.IntegerField(min_value=1, max_value=6)
    userProg = serializers.IntegerField()
    userPhone = serializers.CharField(max_length=20)
    userMail = serializers.CharField(max_length=50)
    userFunctionType = serializers.CharField(max_length=1)
    verificationCode = serializers.CharField(max_length=16)


class ServiceFiveSerializer(serializers.Serializer):
    callType = serializers.IntegerField(min_value=1, max_value=6)
    userProg = serializers.IntegerField()
    userMail = serializers.CharField(max_length=50)
    userName = serializers.CharField(max_length=3)
    regAcceptTermsCondition = serializers.CharField(max_length=1)
    regAcceptPrivacy = serializers.CharField(max_length=1)
    regAcceptStatistics = serializers.CharField(max_length=1)
    appID = serializers.CharField(max_length=3)
    appAcceptTermsCondition = serializers.CharField(
        required=False, max_length=1)
    appAcceptPrivacy = serializers.CharField(required=False, max_length=1)
    appAcceptStatistics = serializers.CharField(required=False, max_length=1)
    password = serializers.CharField(max_length=16)
    userFunctionType = serializers.CharField(max_length=1)


class ServiceSixSerializer(serializers.Serializer):
    callType = serializers.IntegerField(min_value=1, max_value=6)
    userProg = serializers.IntegerField()
    userMail = serializers.CharField(max_length=50)
    userLanguage = serializers.CharField(max_length=2)
    promoCode = serializers.CharField(required=False, max_length=10)


class ServiceSevenSerializer(serializers.Serializer):
    callType = serializers.IntegerField(min_value=1, max_value=6)
    language = serializers.CharField(max_length=2)
    ownerId = serializers.IntegerField()
    ownerCountryCode = serializers.CharField(max_length=2)


class REG008(serializers.Serializer):
    callType = serializers.IntegerField(min_value=1, max_value=6)
    userProg = serializers.IntegerField()
    userMail = serializers.CharField(max_length=50)
    userPhone = serializers.CharField(max_length=20)
    userFunctionType = serializers.CharField(max_length=1)
    verificationCode = serializers.CharField(max_length=16)


class LoginSerializer(serializers.Serializer):
    userProg = serializers.IntegerField()
    password = serializers.CharField(max_length=16)
    functionType = serializers.CharField(max_length=1)


class SendVerCodeSerializer(serializers.Serializer):
    userFunctionType = serializers.CharField(max_length=1)
    userProg = serializers.IntegerField()
    userMail = serializers.CharField(max_length=50)
    userPhone = serializers.CharField(max_length=20)


class PhoneSerializerVerify(serializers.Serializer):
    phone_userProg = serializers.IntegerField()
    phone_userPhone = serializers.CharField(max_length=20)
    phone_verificationCode = serializers.CharField(max_length=16)
    phone_callType = serializers.CharField(max_length=1)


class PhoneSerializer(serializers.Serializer):
    phone_userProg = serializers.IntegerField()
    phone_userPhone = serializers.CharField(max_length=20)
    phone_callType = serializers.CharField(max_length=1)


class RegCustomerSerializer(serializers.Serializer):
    userProg = serializers.IntegerField()


class RegCustomerSurnameSerializer(serializers.Serializer):
    userProg = serializers.IntegerField()
    surname = serializers.CharField(max_length=30)


class RegCustomerNameSerializer(serializers.Serializer):
    userProg = serializers.IntegerField()
    name = serializers.CharField(max_length=30)


class RegCustomerBdateSerializer(serializers.Serializer):
    userProg = serializers.IntegerField()
    bdate = serializers.DateField()


class ListCountrySerializer(serializers.Serializer):
    language = serializers.CharField(max_length=2)
    ownerId = serializers.IntegerField()


class ListFriendsSerializer(serializers.Serializer):
    countryCode = serializers.CharField(max_length=2)
    language = serializers.CharField(max_length=2)
    ownerId = serializers.IntegerField()
