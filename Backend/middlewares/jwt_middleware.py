import datetime
import jwt
from django.http import JsonResponse
from django.conf import settings
import os

JWT_SECRET_KEY = "q7Z$9rG!uP@3tM^jK8bV&5wL#fR2eC*1"
USERNAME = "malardalenUniversity"
PASSWORD = "vA8#xN7$zP9!wQ6@tJ4"

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempted_paths = ['/api/health', '/api/generate_token']

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            print("Error: Token has expired")
            return {"error": "Token has expired"}
        except jwt.InvalidTokenError:
            print("Error: Invalid token")
            return {"error": "Invalid token"}
        except jwt.PyJWTError as e:
            print("Error decoding token:", str(e))
            return {"error": "Token decoding failed"}
        except Exception as e:
            print("Unexpected error:", str(e))
            return {"error": "An unexpected error occurred"}

    def __call__(self, request):
        if request.path in self.exempted_paths or request.path.rstrip('/') in self.exempted_paths:
            return self.get_response(request)
    
        auth_header = request.headers.get('Authorization', None)

        if not auth_header:
            return JsonResponse({"error": "Authorization token required"}, status=401)

        if auth_header:
            token = auth_header.split(" ")[1]
            decoded_payload = self.decode_token(token)

            if 'error' in decoded_payload:
                return JsonResponse(decoded_payload, status=401)

            username = decoded_payload.get("user")
            password = decoded_payload.get("secret_code")

            if username != USERNAME or password != PASSWORD:
                return JsonResponse({"error": "Invalid credentials"}, status=403)

            request.user_data = decoded_payload

        response = self.get_response(request)
        return response