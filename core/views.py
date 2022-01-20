from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import permission_classes

from core.models import User
import core.serializer as serializers


@permission_classes([])
class RegisterUser(APIView):

    def post(self, request, format=None):
        '''
        Register New User
        '''

        errors = {
            'duplicate_username':
                'Este usuario ya existe, por favor intenta con otro'
        }

        serializer = serializers.RegisterUser(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = \
                make_password(serializer.validated_data['password'])
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            try:
                if serializer.errors['username']:
                    return JsonResponse(errors)
            except KeyError:
                pass


class GetUser(APIView):

    def get(self, request, pk, format=None):
        '''
        Obtiene datos del usuario dado (pk)
        '''

        user = User.objects.get(id=pk)
        serializer = serializers.GetUser(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EditUser(APIView):

    def patch(self, request, pk):

        '''
        Before saving, it is checked if the username already exists,
        if so, an error message is returned.
        If not, then the data is saved.
        '''
        errors = {
            'duplicate_username':
            'Este usuario ya existe, por favor intenta con otro'
        }
        user = User.objects.get(pk=pk)
        is_ok = False
        try:
            duplicate_user = User.objects.get(
                username=request.data["username"])
            if duplicate_user.id == user.id:
                is_ok = True
        except Exception:
            is_ok = True
        if is_ok:
            serializer = serializers.EditUser(
                user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_200_OK)
        else:
            return Response(data=errors)


class UpdatePictures(APIView):

    def patch(self, request, pk):
        '''
        Update your profile or cover images
        '''
        user = User.objects.get(pk=pk)

        serializer = serializers.UpdatePictures(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_200_OK)


class UpdatePassword(APIView):

    def patch(self, request, pk):

        user = User.objects.get(pk=pk)
        serializer = serializers.UpdatePassword(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['password'] = \
                make_password(serializer.validated_data['password'])
            serializer.save()
            return Response(status=status.HTTP_200_OK)
