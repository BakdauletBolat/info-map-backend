from rest_framework.authtoken.models import Token
from rest_framework import decorators


@decorators.action(methods=["GET"], detail=False)
def get_user(request):
    token_header = request.headers.get("Authorization")
    token = token_header.split(" ")[1]
    token_model = Token.objects.get(key=token)
    return {
        "user": token_model.user.username,
        "id": token_model.user.id
    }
