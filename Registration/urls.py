from django.urls import path
from . import REG001PREREG
from Community import CMTY001, CMTY002, CMTY003
from Registration import REG004PHONEVERIFY


urlpatterns = [
    path('reg001prereg', REG001PREREG.mainService),
    path('reg004verify', REG004PHONEVERIFY.REG004PHONEVERIFY),
    path('cmty001', CMTY001.CMTY001),
    path('cmty002', CMTY002.CMTY002),
    path('cmty003', CMTY003.CMTY003)
]
