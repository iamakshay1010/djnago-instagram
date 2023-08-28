from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializer import UserLoginSerializer, UserSerializer
from app.models import User
from rest_framework.authtoken.models import Token

#imorting stuff here



class Akshay(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class= UserSerializer

class LoginUserView(APIView):

    def post(self, request):
        # request.data (email, password)
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data["email"])
                if user.password == serializer.validated_data["password"]:
                    token = Token.objects.get_or_create(user=user)
                    return Response({ "success": True, "token": token[0].key })
                else:
                    return Response({ "success": False, "message": "incorrect password" })



            except ObjectDoesNotExist:
                return Response({ "success": False, "message": "user does not exist" })
            
