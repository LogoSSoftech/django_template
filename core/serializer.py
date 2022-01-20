from rest_framework import serializers

from core.models import User


class Users(serializers.ModelSerializer):

    '''
   General serializer to use Djoser
    '''

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'profile_picture',
            'profile_cover',
            'is_superuser',
        ]


class RegisterUser(serializers.ModelSerializer):

    '''
   To Register and Auth Users
    '''

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
        ]


class EditUser(serializers.ModelSerializer):

    '''
   To Edit User Data
    '''

    full_name = serializers.SerializerMethodField('get_user_full_name')

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'full_name',
            'first_name',
            'last_name',
        ]

    def get_user_full_name(self, obj):
        return obj.get_full_name()


class UpdatePassword(serializers.ModelSerializer):

    '''
   To Update Password
    '''

    class Meta:
        model = User
        fields = [
            'id',
            'password',
        ]


class UpdatePictures(serializers.ModelSerializer):

    '''
   To Update Pictures
    '''

    class Meta:
        model = User
        fields = [
            'profile_picture',
            'profile_cover',
        ]


class GetUser(serializers.ModelSerializer):

    '''
   To Get User Data
    '''

    full_name = serializers.SerializerMethodField('get_user_full_name')

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'full_name',
            'first_name',
            'last_name',
            'profile_picture',
            'profile_cover',
            'is_superuser',
        ]

    def get_user_full_name(self, obj):
        return obj.get_full_name()
