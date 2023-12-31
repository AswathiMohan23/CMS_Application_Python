from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from user_app.serializer import RegistrationSerializer, LoginSerializer


class UserRegistration(viewsets.ViewSet):

    def create(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Registration completed", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)


class UserLogin(viewsets.ViewSet):

    serializer_class = LoginSerializer
    def create(self, request):
        try:
            serializer = LoginSerializer(data=request.data,context={'request':request})

            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "login successful", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)
