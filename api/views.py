from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import status
from .models import User
import requests, os

class Users(APIView):
    def post(self, request):
        name = request.get('name')
        email = request.get('email')
        cpf = request.get('cpf')

        try:
             User.objects.create(
                cpf = cpf,
                name = name,
                email = email
            )

        except Exception as e:
            return Response({'saved': f'Não foi possível salvar no banco de dados? {e}'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status = 200)

    def put(self, request):
        phone = request.get('phone')
        age = request.get('age')

        try:
             User.objects.create(
                phone = phone,
                age = age
            )

        except Exception as e:
            return Response({'saved': f'Não foi possível salvar no banco de dados? {e}'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status = 200)

    def get(self, request, id = None):
        if id is not None:
            return self.retrieve(request)

        return self.list(request)

    def delete(self, request, id):
        user = get_object_or_404(User, id = id)

        email = request.get('email')
        phone = request.get('phone')
        age = request.get('age')
        name = request.get('name')

        for field, value in (('email', email), ('phone', phone), ('age', age), ('name', name)):
            setattr(user, field, value)

        user.save(update_fields=['email', 'phone_number', 'age', 'name'])

        return Response(status = 200)