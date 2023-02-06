from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from Registration.serializers import *
from user.models import *
from user.serializers import CountryCodeSerializer, UserSerializer, UserAppSerializer
from datetime import datetime


def CMTY002(request):
    ListCountrySerializer = ListCountrySerializer(data=request.data)
    err = errorCodes.error_codes
    if ListCountrySerializer.is_valid() == False:
        return Response({"errId": 2, "errMessage": err[30], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        country_model = CountryModel.objects.using("db999_services").filter(
            cmty_ownerid=ListCountrySerializer.data["owner_id"]).values_list('cmty_country', flat=True).distinct()
        countries = CountryModel.objects.using("db992_community").filter(
            country_countrycode=country_model).order_by('country_name')
        data = [{'country_countrycode': country.country_countrycode,
                 'country_name': country.country_name} for country in countries]
    except:
        # db_error'den emin ol
        return Response({"errId": 32, "errMessage": err[31], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
