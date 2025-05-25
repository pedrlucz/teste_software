from rest_framework import generics, mixins, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.http import HttpResponse
from .models import User

class Users(mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    """"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

    def post(self, request):
        payload = request.data

        name = payload.get('name')
        email = payload.get('email')
        cpf = payload.get('cpf')

        try:
             User.objects.create(
                cpf = cpf,
                name = name,
                email = email
            )

        except Exception as e:
            return Response({'saved': f'Não foi possível salvar no banco de dados? {e}'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response('Novo usuário salvo!', status = 200)

    def put(self, request, id):
        payload = request.data

        phone = payload.get('phone')
        age = payload.get('age')

        user = get_object_or_404(User, id = id)

        try: 
            user.phone = phone
            user.age = age 

            user.save(update_fields=['phone', 'age'])

        except Exception as e:
            return Response({'saved': f'Não foi possível salvar no banco de dados? {e}'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response('Usuário atualizado!', status = 200)

    def get(self, request, id = None):
        if id is not None:
            return self.retrieve(request, id = id)

        return self.list(request)

    def delete(self, request, id):
        payload = request.data

        user = get_object_or_404(User, id = id)
        user.delete()

        # depois ver se consigo fazer
        # email = payload.get('email')
        # phone = payload.get('phone')
        # age = payload.get('age')
        # name = payload.get('name')

        # for field, value in (('email', email), ('phone', phone), ('age', age), ('name', name)):
        #     setattr(user, field, value)

        # user.save(update_fields=['email', 'phone_number', 'age', 'name'])

        return Response(status = 200)