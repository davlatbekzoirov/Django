from .models import User, UserConfirmation, VIA_EMAIL, VIA_PHONE, CODE_VERIFIED, DONE, NEW, PHOTO_STEP
from rest_framework import exceptions
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class SignUpSerialazer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    def __init__(self, *args, **kwargs):
        super(SignUpSerialazer, self).__init__(*args, **kwargs)
        self.fields['email_phone_number'] = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'id', 'auth_type', 'auth_status'
        )
        extra_kwargs = {
            'auth_type': {'read_only': True, 'required': False},
            'auth_status': {'read_only': True, 'required': False}
        }

    def validate(self, data):
        super(SignUpSerialazer, self).validate(data)
        data = self.auth_validate(data)
        return data

    @staticmethod
    def auth_validate(data):
        print(data)
        user_input = str(data.get('email_phone_number')).lower()
        return data