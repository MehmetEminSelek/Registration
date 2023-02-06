from django.db import models
import uuid
# import qrcode
from io import BytesIO
from django.core.files import File
# from PIL import Image, ImageDraw
# ALL PROGS SHOULD BE PRIMARY KEY
# USER PRESENTERID SHOULD BE CHARFIELD WITH 16 CHARACTERS
# NO AUTOFIELDS INSTED OF THAT WE ARE GOING TO USE INTEGERFIELD WITH PRIMARY KEY


class UserModel(models.Model):
    user_Prog = models.AutoField(primary_key=True)
    user_Mail = models.CharField(max_length=50, unique=True)
    user_CountryCode = models.CharField(max_length=2)
    user_Language = models.CharField(max_length=2)
    user_PresenterID = models.IntegerField(default=0, blank=True, null=True)
    user_mailStatus = models.CharField(max_length=1, default='N')
    user_Status = models.IntegerField(null=True, blank=True)
    user_phonePrefix = models.CharField(max_length=7, blank=True, null=True)
    user_Language = models.CharField(max_length=2, blank=True, null=True)
    user_phoneNumber = models.IntegerField(
        null=True, blank=True)
    user_acceptTermsCondition = models.CharField(
        max_length=1, blank=True, default='N')
    user_acceptPrivacy = models.CharField(
        max_length=1, blank=True, default='N')
    user_acceptStatistics = models.CharField(
        max_length=1, blank=True, default='N')
    user_promoCode = models.CharField(max_length=10, blank=True, default='N')
    user_userID = models.CharField(blank=True, null=True, max_length=50)
    user_functionType = models.CharField(max_length=1, blank=True, null=True)
    user_Type = models.CharField(max_length=2, blank=True, null=True)
    user_mail2 = models.CharField(max_length=50, blank=True, null=True)
    user_maildelegat = models.CharField(max_length=50, blank=True, null=True)
    user_phonenumber2 = models.IntegerField(
        null=True, blank=True)
    user_username = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return str(self.user_username)


class LanguageModel(models.Model):
    value = models.CharField(max_length=2)

    class Meta:
        db_table = 'language'

    def __str__(self) -> str:
        return self.value


class CountryModel(models.Model):
    country_coutrycode = models.CharField(max_length=2)
    country_name = models.CharField(max_length=14)
    country_phoneprefix = models.CharField(max_length=4)

    class Meta:
        db_table = 'country'


    def __str__(self) -> str:
        return self.country_coutrycode

# TODO: add primary key
class UserApp(models.Model):
    userProg = models.IntegerField(blank=True, null=True)
    appID = models.IntegerField(blank=True, null=True)
    userStatus = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user_app'

    def __str__(self) -> int:
        return str(self.appID)


class VerificationCodeModel(models.Model):
    verUserProg = models.IntegerField()
    verCodeType = models.CharField(max_length=1)
    verStartDate = models.DateTimeField()
    verEndDate = models.DateTimeField()
    verlastLoginerr = models.DateTimeField(null=True, blank=True)
    verstatus = models.CharField(max_length=1)
    vercterr = models.IntegerField(null=True, blank=True)
    verlasttentative = models.DateTimeField(null=True, blank=True)
    verificationCode = models.CharField(max_length=6, default='000000')

    class Meta:
        db_table = 'verification_code'

    def __str__(self) -> str:
        return self.verificationCode


class PasswordModel(models.Model):
    passwordPassword = models.CharField(max_length=50)
    passwordUserProg = models.IntegerField()
    passworduserMail = models.CharField(max_length=50)
    passwordStatus = models.CharField(max_length=1)
    passwordLastLogin = models.DateTimeField()
    passwordEndDate = models.DateTimeField()
    passwordStartDate = models.DateTimeField()
    passwordCterr = models.IntegerField()

    class Meta:
        db_table = 'password'

    def __str__(self) -> str:
        return self.password

# TODO: PRimary key as customer prog


class CustomerModel(models.Model):
    cus_progr = models.IntegerField(primary_key=True)
    cus_name = models.CharField(max_length=30, blank=True, null=True)
    cus_surname = models.CharField(max_length=30, blank=True, null=True)
    cus_address = models.CharField(max_length=200, blank=True, null=True)
    cus_birthdate = models.DateField(blank=True, null=True)
    cus_docimgfrontid = models.CharField(max_length=10, blank=True, null=True)
    cus_docimgackid = models.CharField(max_length=10, blank=True, null=True)
    cus_residenceproofimg = models.CharField(
        max_length=10, blank=True, null=True)
    cus_docendvalidity = models.DateField(blank=True, null=True)
    cus_nationalid = models.CharField(max_length=30, blank=True, null=True)
    cus_companyprogr = models.IntegerField(null=True, blank=True)
    cus_companyrole = models.CharField(
        max_length=15, choices=[('list of value', 'list of value')], blank=True, null=True)
    cus_companyauthlevel = models.CharField(
        max_length=15, choices=[('list of value', 'list of value')], blank=True, null=True, default=0)

    class Meta:
        db_table = 'customer'

    def __str__(self) -> str:
        return self.cus_name


class CompanyModel(models.Model):
    comp_prog = models.IntegerField(primary_key=True)
    comp_mail = models.CharField(max_length=50, blank=True, null=True)
    comp_name = models.CharField(max_length=100, blank=True, null=True)
    comp_address = models.CharField(max_length=200, blank=True, null=True)
    comp_legalrepprogr = models.IntegerField(blank=True, null=True)
    comp_legalrepname = models.CharField(max_length=30, blank=True, null=True)
    comp_legalrepsurname = models.CharField(
        max_length=30, blank=True, null=True)
    comp_legalrpcountry = models.CharField(max_length=2, blank=True, null=True)
    comp_legalrepmail = models.CharField(max_length=50, blank=True, null=True)
    comp_legalrepdocimgfrontid = models.CharField(
        max_length=10, blank=True, null=True)
    comp_legalrepdocimgackid = models.CharField(
        max_length=10, blank=True, null=True)
    comp_vatcode = models.CharField(max_length=30, blank=True, null=True)
    comp_sectorid = models.CharField(max_length=3,  blank=True, null=True)
    comp_legalrepdocendvalidity = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'company'

    def __str__(self) -> str:
        return self.comp_name


class ExpertModel(models.Model):
    user_id = models.IntegerField(unique=True)
    exp_prog = models.IntegerField()
    expert_mail = models.EmailField(unique=True)
    business_name = models.CharField(max_length=30)
    document_type = models.CharField(max_length=2)
    document_id = models.CharField(max_length=15)
    document_image_front = models.ImageField()
    document_image_back = models.ImageField()
    vat_code = models.CharField(max_length=30)
    job_sector_id = models.CharField(max_length=3)

    class Meta:
        db_table = 'expert'

    def __str__(self) -> str:
        return self.business_name


class App(models.Model):
    app_appid = models.CharField(max_length=3, unique=True)
    app_name = models.CharField(max_length=15)
    app_description = models.CharField(max_length=100)
    app_status = models.BooleanField()
    app_link = models.CharField(max_length=60)
    app_usertypeauth = models.CharField(max_length=1)
    app_startdate = models.DateField()
    app_enddate = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'app'

    def __str__(self) -> str:
        return self.app_name


class PlanApp(models.Model):
    plan = models.CharField(max_length=10, unique=True)
    app_code = models.CharField(max_length=3, unique=True)
    status = models.BooleanField()
    plan_name = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.PositiveSmallIntegerField()
    duration_type = models.CharField(max_length=1)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'plan_app'

    def __str__(self) -> str:
        return self.plan_name


class PlanDetails(models.Model):
    plan = models.CharField(max_length=10)
    row_progr = models.PositiveSmallIntegerField(unique=True)
    field_name = models.CharField(max_length=10)
    field_type = models.CharField(max_length=1)
    field_value = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'plan_details'

    def __str__(self) -> str:
        return self.plan + self.row_progr


class Profile(models.Model):
    profile = models.CharField(max_length=10, unique=True)
    app_code = models.CharField(max_length=3, unique=True)
    status = models.BooleanField()
    profile_name = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'profile'

    def __str__(self) -> str:
        return self.profile_name


class PromoCode(models.Model):
    promo_promocode = models.CharField(max_length=10, unique=True)
    promo_appid = models.CharField(max_length=3, unique=True)
    promo_desc = models.CharField(max_length=100)
    promo_status = models.BooleanField()
    promo_startdate = models.DateField()
    promo_enddate = models.DateField()

    class Meta:
        db_table = 'promo_code'

    def __str__(self) -> str:
        return self.promo_promocode


class UserPayMet(models.Model):
    user_id = models.PositiveIntegerField(unique=True)
    payment_method = models.CharField(max_length=3)
    payment_method_progr = models.PositiveSmallIntegerField(unique=True)
    payment_method_id = models.CharField(max_length=30)
    payment_method_user_note = models.CharField(
        max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'paymet'

    def __str__(self) -> str:
        return self.payment_method


class ChangePhone(models.Model):
    phone_userprogr = models.IntegerField(default=0, blank=True, null=True)
    phone_status = models.CharField(
        max_length=20, choices=[('list of value', 'list of value')])
    phone_number = models.DecimalField(max_digits=20, decimal_places=0)
    phone_endverification = models.DateTimeField(blank=True, null=True)
    phone_endvalidity = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'change_phone'

    def __str__(self) -> str:
        return self.phone_number

class CommunityModel(models.Model):
    cmty_ownerid = models.IntegerField(default=0, blank=True, null=True)
    cmty_country = models.CharField(max_length=2)
    cmty_memberid = models.IntegerField(default=0, blank=True, null=True)
    cmty_cmtylevel = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    cmty_status = models.CharField(max_length=1, choices=[(
        'P', 'Pending'), ('A', 'Approved'), ('C', 'Cancelled')])
    cmty_insertdate = models.DateTimeField(auto_now_add=True)
    cmty_lastupdate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'community'


class RewardsModel(models.Model):
    hrew_userid = models.IntegerField(
        default=0, blank=True, null=True)  # populate by hand
    hrew_period = models.CharField(max_length=7, null=True, blank=True)
    hrew_country = models.CharField(max_length=2, null=True, blank=True)
    hrew_friendscount = models.IntegerField(null=True, blank=True)
    hrew_cmtycount = models.IntegerField(null=True, blank=True)
    hrew_userrp = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True)
    hrew_cmtyrp = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True)
    hrew_userevel = models.DecimalField(
        max_digits=2, decimal_places=0, null=True, blank=True)
    hrew_levelperc = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    hrew_userearn = models.DecimalField(
        max_digits=11, decimal_places=2, null=True, blank=True)
    hrew_insertdate = models.DateTimeField(auto_now_add=True)
    hrew_lastupdate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'rewards'


class errorCodes:
    error_codes = [
        {'RC': 1, 'description': 'Wrong call type'},
        {'RC': 2, 'description': 'Missing mandatory data'},
        {'RC': 3, 'description': 'User_mail already registered'},
        {'RC': 4, 'description': [{"1": "Waiting for mail validation"}, {"2": "Waiting for phone validation"}, {
            "3": "Waiting for additional info from pe-registration"}, {"4": "Waiting for additional info from pe-registration"}, {"5": "Pre-registration phase completed"}]},
        {'RC': 5, 'description': 'Invalid Country code'},
        {'RC': 6, 'description': 'Presenter not valid'},
        {'RC': 7, 'description': 'Unsuccessfull mail validation'},
        {'RC': 8, 'description': 'Unsuccessfull insert table'},
        {'RC': 9, 'description': 'User mail not valid'},
        {'RC': 10, 'description': 'Unsuccessfull update table'},
        {'RC': 12, 'description': 'Unsuccessfull phone validation'},
        {'RC': 13, 'description': 'Invalid Application Code'},
        {'RC': 14, 'description': 'Unsuccessfull password validation'},
        {'RC': 16, 'description': 'Unsuccessfull ID creation'},
        {'RC': 17, 'description': 'Password already registered'},
        {'RC': 18, 'description': 'Password not numeric'},
        {'RC': 19, 'description': 'Invalid old password'},
        {'RC': 20, 'description': 'Invalid password'},
        {'RC': 21, 'description': 'Expired password'},
        {'RC': 22, 'description': 'Locked password'},
        {'RC': 23, 'description': 'Invalid verification code'},
        {'RC': 24, 'description': 'Locked verification code'},
        {'RC': 25, 'description': 'Expired verification code'},
        {'RC': 26, 'description': 'Invalid Promo'},
        {'RC': 28, 'description': 'Failed Verification code'},
        {'RC': 29, 'description': 'Missing error code'},
        {'RC': 30, 'description': 'UserID not valid'},
        {'RC': 31, 'description': 'Mandatory data not present'},
        {'RC': 32, 'description': 'Select community owner'},
        {'RC': 33, 'description': 'Data not valid'}
    ]

    class Meta:
        db_table = 'error_codes'


abs = [{
    'RC': 1,
    'description': [{'Wrong call type'}, {"asd": "asd"}]
}]
