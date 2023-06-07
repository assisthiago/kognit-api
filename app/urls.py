from django.urls import include, path
from rest_framework import routers

from app.core.views import UserModelViewSet, WalletModelViewSet


router = routers.DefaultRouter()
router.register(r'users', UserModelViewSet)
router.register(r'wallets', WalletModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
