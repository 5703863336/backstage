def jwt_response_payload_handler(token, user, request):

    return {
        'id':user.id,
        'username':user.username,
        'token':token
    }