from rest_framework import viewsets

from app.core.models import User, Wallet
from app.core.serializers import UserSerializer, WalletSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    # CRUD views
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WalletModelViewSet(viewsets.ModelViewSet):
    # CRUD views
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def get_queryset(self):
        queryset =  Wallet.objects.all()

        if user := self.request.query_params.get('user'):
            queryset = queryset.filter(user__id=user)

        return queryset
