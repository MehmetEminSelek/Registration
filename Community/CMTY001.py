from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from Registration.serializers import *
from user.models import *
from user.serializers import CountryCodeSerializer, UserSerializer, UserAppSerializer
from datetime import datetime


def CMTY001(request):
    serviceSevenSerializer = ServiceSevenSerializer(data=request.data)
    err = errorCodes.error_codes
    if serviceSevenSerializer.is_valid() == False:
        return Response({"errId": 1, "errMessage": err[0], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if serviceSevenSerializer.data["userPresenterId"] != "":
        if UserModel.objects.get(user_PresenterId=serviceSevenSerializer.data["userPresenterId"]).user_Prog != serviceSevenSerializer.data["userPresenterId"]:
            return Response({"errId": 6, "errMessage": err[5], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        input_user = UserModel.objects.get(
            user_Prog=serviceSevenSerializer.data["userPresenterID"])
        presenter_country = input_user.user_CountryCode
    except:
        return Response({"errId": 9, "errMessage": err[8], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if serviceSevenSerializer.data["ownerCountryCode"] == presenter_country:
        PROCSAMECOUNTRY(serviceSevenSerializer.data)
    else:
        PROCSAMECOUNTRY(serviceSevenSerializer.data)


def PROCSAMECOUNTRY(userData):
    country_data = userData.data
    level = 0
    try:
        CommunityModel.objects.create(
            cmty_ownerid=country_data["ownerid"],
            cmty_country=country_data["ownerCountryCode"],
            cmty_memberid=country_data["ownerid"],
            cmty_cmtylevel=level)
    except:
        return Response({"errId": 10, "errMessage": "dbError:isrt community owner", "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    try:
        RewardsModel.objects.using("community").create(
            hrew_userid=country_data["ownerid"],
            hrew_period=year + "-" + month,
            hrew_country=country_data["ownerCountryCode"],
            hrew_cmtycount=1,
            hrew_lastupdate=datetime.datetime.now())
    except:
        return Response({"errId": 10, "errMessage": "dbError:isrt rewards point", "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        update_data = CommunityModel.objects.using("community").filter(cmty_memberid=country_data["presenterid"]).filter(
            cmty_country=country_data["ownerCountryCode"]).order_by("-cmty_cmtylevel")
    except:
        return Response({"errId": 10, "errMessage": "dbError:select community", "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        # owner?
        update_data.cmty_ownerid = update_data.cmty_ownerid
        update_data.cmty_memberid = country_data["ownerid"]
        update_data.cmty_cmtylevel = update_data.cmty_cmtylevel + 1
        update_data.cmty_status = "P"
        update_data.save()
    except:
        return Response({"errId": 10, "errMessage": "dbError:update community", "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    # UPDATE REWARDS POINT
    try:
        community = CommunityModel.objects.using(
            "community").filter(cmty_cmtylevel=1).filter(cmty_memberid=country_data["ownerid"]).filter(cmty_country=country_data["ownerCountryCode"])
    except:
        return Response({"errId": 10, "errMessage": "dbError:select community", "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        rewards_updated = RewardsModel.objects.using("community").filter(
            hrew_userid=community.cmty_ownerid).filter(hrew_country=country_data["ownerCountryCode"])
        rewards_updated.hrew_cmtycount = rewards_updated.hrew_cmtycount + 1
        rewards_updated.hrew_friendscount = rewards_updated.hrew_friendscount + 1
        rewards_updated.hrew_lastupdate = datetime.datetime.now()
        rewards_updated.save()
    except:
        return Response({"errId": 10, "errMessage": "dbError:update rewards", "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        # CMTY_CMTYLEVEL__GT IS GREATER THAN FOR LESS THAN USE CMTY_CMTYLEVEL__LT FOR GREATER OR EQUAL USE CMTY_CMTYLEVEL__GTE
        community_1 = CommunityModel.objects.using(
            "community").filter(cmty_cmtylevel__gt=1).filter(cmty_memberid=country_data["ownerid"]).filter(cmty_country=country_data["ownerCountryCode"])
    except:
        return Response({"errId": 10, "errMessage": "dbError:select community", "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        rewards_updated = RewardsModel.objects.using("community").filter(
            hrew_userid=community_1.cmty_ownerid).filter(hrew_country=country_data["ownerCountryCode"])
        rewards_updated.hrew_cmtycount = rewards_updated.hrew_cmtycount + 1
        rewards_updated.hrew_friendscount = rewards_updated.hrew_friendscount + 1
        rewards_updated.hrew_lastupdate = datetime.datetime.now()
        rewards_updated.save()
    except:
        return Response({"errId": 10, "errMessage": "dbError:update rewards", "RC": 99}, status=status.HTTP_400_BAD_REQUEST)


def PROCDIFFCOUNTRIES(userData):
    country_data = userData.data
    level = 0
    err = errorCodes.error_codes
    if CommunityModel.objects.using("community").filter(cmty_ownerid=country_data["userPresenterId"]).filter(cmty_country=country_data["ownerCountryCode"]).filter(cmty_cmtylevel=level).exists() == True:
        return Response({"errId": 0, "status": "success", "RC": 0}, status=status.HTTP_200_OK)
    # ISRTCOMMPRESS
    try:
        community = CommunityModel.objects.using("community").filter(cmty_memberid=country_data["userPresenterId"]).filter(
            cmty_country=country_data["ownerCountryCode"]).order_by("-cmty_ownerid").order_by("cmty_cmtylevel")
    except:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    # saved_ownerid == community.cmty_ownerid ?

    if CommunityModel.objects.using("community").filter(cmty_ownerid=community.cmty_ownerid).exists == True:
        if CommunityModel.objects.using("community").filter(cmty_ownerid=community.cmty_ownerid).filter(cmty_country=country_data["ownerCountryCode"]).filter(cmty_memberid=country_data["userPresenterId"]).exists == False:
            try:
                CommunityModel.objects.using("community").create(
                    cmty_ownerid=community.cmty_ownerid,
                    cmty_memberid=country_data["userPresenterId"],
                    cmty_country=country_data["ownerCountryCode"],
                    cmty_cmtylevel=level,
                    cmty_status="A")
            except:
                return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    if RewardsModel.objects.using("community").filter(hrew_userid=community.cmty_ownerid).filter(hrew_country=country_data["ownerCountryCode"]).filter(hrew_period=datetime.now().year + datetime.now().month).exists == False:
        try:
            year = datetime.now().year
            month = datetime.now().month
            period = year + month
            RewardsModel.objects.using("community").create(
                hrew_userid=community.cmty_ownerid,
                hrew_period=period,
                hrew_country=country_data["ownerCountryCode"],
                hrew_cmtycount=1,
                hrew_lastupdate=datetime.now(),
                hrew_insertdate=datetime.now())
            # friendscount ??
        except:
            return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        ctr_friends = CommunityModel.objects.using("community").filter(cmty_ownerid=community.cmty_ownerid).filter(
            cmty_country=country_data["ownerCountryCode"]).filter(cmty_cmtylevel=1).count()
    except:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        ctr_cmty = CommunityModel.objects.using("community").filter(
            cmty_ownerid=community.cmty_ownerid).filter(cmty_country=country_data["ownerCountryCode"]).count()
    except:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
    try:
        rewards_updated = RewardsModel.objects.using("community").filter(hrew_userid=community.cmty_ownerid).filter(
            hrew_country=country_data["ownerCountryCode"]).filter(hrew_period=period)
        rewards_updated.hrew_cmtycount = ctr_cmty
        rewards_updated.hrew_friendscount = ctr_friends
        rewards_updated.hrew_lastupdate = datetime.now()
        rewards_updated.save()
    except:
        return Response({"errId": 2, "errMessage": err[1], "RC": 99}, status=status.HTTP_400_BAD_REQUEST)
