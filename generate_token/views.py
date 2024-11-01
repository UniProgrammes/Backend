from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
import jwt

JWT_SECRET_KEY = "q7Z$9rG!uP@3tM^jK8bV&5wL#fR2eC*1"
ACCESS_TOKEN_LIFETIME = 60 * 60

USERNAME = "malardalenUniversity"
PASSWORD = "vA8#xN7$zP9!wQ6@tJ4"

class GenerateTokenView(APIView):
    def get(self, request):
        
        payload = {
            'user': USERNAME,
            'secret_code': PASSWORD, 
            'exp': datetime.now() + timedelta(seconds=ACCESS_TOKEN_LIFETIME),
            'iat': datetime.now(),
            'token_type': 'bearer'
        }

        accessToken = jwt.encode(payload, JWT_SECRET_KEY, "HS256")

        return Response({"token_type": "bearer", "access_token": accessToken}, status=status.HTTP_200_OK)