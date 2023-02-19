from rest_framework import serializers
import json
from server.models import Account
import random

class RegisterSerializer(serializers.Serializer):
    file = serializers.FileField()

    def create(self, validated_data):
        users = json.load(validated_data['file'])

        for user in users:
            print(user)
            password = Account.objects.make_random_password()
            if user['phone_number'] == '':
                phone = '123'
            else:
                phone = str(user['phone_number']).split('\n')[0]
            account = Account.objects.create(
                username=user['username'] + str(random.randint(1000, 9999)),
                first_name=user['first_name'],
                living_place=user['living_place'],
                nation=user['nation'],
                occupation=user['occupation'],
                phone_number=phone,
                new_password=password,
            )
            account.set_password(password)
            account.save()
        return account
