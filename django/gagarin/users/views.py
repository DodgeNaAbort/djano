from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework import status

class RegisterView(APIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            return Response({
                "data": {
                    "user": {
                        "name": f"{user.last_name} {user.first_name} {user.patronymic}",
                        "email": user.email
                    },
                    "code": 201,
                    "message": "Пользователь создан"
                }
            }, status=status.HTTP_201_CREATED)