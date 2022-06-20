from rest_framework.views import APIView, Response
from .serializers import RegistrationSerializer, LoginSerializers, ResetPassSerializer
from django.contrib.auth import get_user_model, authenticate, login, logout
from common.jwt_token import get_token, token_required
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Utils
from .validators import validate_password, validate_login, validate_register
from django.utils.decorators import method_decorator

User = get_user_model()


class RegistrationApiView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = User.objects.create_user(username=username, email=email, password=password, is_active=False)
        user.save()
        token = get_token(user).get('access')
        short_token = Utils.token_short(token)
        domain = get_current_site(request).domain
        relative_link = reverse('activate')
        surl = 'http://' + domain + relative_link + '?token=' + short_token
        # email_body = f'Hii {user.username} Use below link to activate your account \n{surl}'
        # data = {'email_body': email_body, 'subject': 'Activate your Account', 'email': user.email}
        # Utils.send_mail(data)
        return Response(
            {'Message': 'User added and click activate link to activate account',
             'Code': 200,
             'activate_link': surl})


class LoginApiView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        data = request.data
        # print(type(data))
        serializer = LoginSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({'Error': 'Check your email and password', 'Code': 401})
        login(request, user)
        token = get_token(user)
        return Response({'Message': 'User Logged in', 'Code': 200, 'token': token})


class LogoutApiView(APIView):
    def get(self, request):
        logout(request)
        return Response({'Message': 'Logged Out', 'Code': 200})


class ResetPassApiView(APIView):
    authentication_classes = ()

    def post(self, request):
        data = request.data
        serializer = ResetPassSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = validate_password(request, serializer)
        if 'Error' in validated_data:
            return Response(validated_data)
        user_obj = User.objects.get(username=validated_data.data.get('username'))
        user_obj.set_password(validated_data.data.get('new_password'))
        user_obj.save()
        return Response({'Message': 'Password Updated', 'Code': 200})


class GetAllUser(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.all()
            serializer = RegistrationSerializer(user, many=True)
            return Response({'users': serializer.data, 'Code': 200})
        return Response({'Error': 'You have to login first', 'Code': 412})


class ActivateApiView(APIView):

    @method_decorator(token_required)
    def get(self, request, user_id):
        # user_id = token_decode(request)
        # if not type(user_id) == int:
        #     return Response(user_id)
        user = User.objects.get(pk=user_id)
        user.is_active = True
        user.save()
        return Response({'Message': 'Account is activated now you can login', 'Code': 200})
