from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class Routes(APIView):
    def get(self, request):
        routes = [
            'api/token',
            'api/token/refresh'
        ]

        return Response(data=routes)