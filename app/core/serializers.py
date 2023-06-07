from rest_framework import serializers

from app.core.models import User, Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['pk', 'amount', 'bank', 'user', 'created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer(many=True, read_only=True)

    def create(self, validated_data):
        # Adds one behavior to the method for lowercase the name.
        validated_data['name'] = validated_data.get('name').lower()
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        super().update(instance, validated_data)

        # Adds one behavior to the method for lowercase the name.
        instance.name = validated_data.get('name', instance.name).lower()
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['pk', 'name', 'birthday', 'cpf', 'wallet', 'created_at', 'updated_at']
