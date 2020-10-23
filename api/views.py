from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.authentication import JWTAuthentication
# import base64
# from rest_framework.generics import RetrieveAPIView
from api.serializer import CategorySerializer, CheckOutSerializer, OrderSerializer, PaymentSerilizer, UserSerializer, UserSigninSerializer, UserSignoutSerializer,\
    CarouselSerializer, GallerySerializer
from api.models import carousel, category, gallery, order, user
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from api.authentication import ExpiringTokenAuthentication
from rest_framework.permissions import AllowAny

# Import Opsi 1
from .authentication import token_expire_handler, expires_in
from rest_framework.authtoken.models import Token 
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from rest_framework.parsers import FileUploadParser
import json
from collections import OrderedDict
from django.http import JsonResponse
import paypalrestsdk
paypalrestsdk.configure({
        'mode': 'live', #sandbox or live
        'client_id': 'Abzv3YdK8zAt03ynlANbg5RtyNBRRRpA4dJt-dF8OXvqycNOiR0U-4uZOVpw3r-ZH-d8dVOhCRXvAjcn',
        'client_secret': 'EHZeutAfPYT0KPpRqahOeTSQhCDUPQvrFGLqwdUMTC76uSUViGjF_SmI_6X1IAA3qVcS8i88P62Wqrmp' })
from paypalrestsdk import Payment
# Create your views here.
        # Untuk hasil url?style=param
        # style = self.request.query_params.get('style', None)
        # Untuk hasil url/param
        # style = self.kwargs['style']
class ApiMenu(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    def get_queryset(self):
        queryset = category.objects.all()
        return queryset

class ApiRegister(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # refresh = RefreshToken.for_user(client)
            # res = {
            #     "refresh": str(refresh),
            #     "access": str(refresh.access_token),
            #         }
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Opsi Pertama Authentikasi
class ApiLogin(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = UserSigninSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        client = authenticate(email=request.data['email'],password=request.data['password'])
        if not client:
            return Response({'detail': 'Invalid Credentials or activate account'}, status=status.HTTP_404_NOT_FOUND)
        client.is_login=True
        client.last_login = timezone.now()
        client.save()
        token, _ = Token.objects.get_or_create(user = client)
        is_expired, token = token_expire_handler(token)
        user_serialized = UserSerializer(client) 
        return Response({
        'user': user_serialized.data, 
        'expires_in': expires_in(token),
        'token': token.key
    }, status=status.HTTP_200_OK)
        
# class ApiLogin(APIView):
#     permission_classes = (AllowAny,)
#     def post(self, request):
#         serializer = UserSigninSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#         client = authenticate(email=request.data['email'],password=request.data['password'])
#         if not client:
#             return Response({'detail': 'Invalid Credentials or activate account'}, status=status.HTTP_404_NOT_FOUND)
#         refresh = RefreshToken.for_user(client) 
#         res = {
#                 "refresh": str(refresh),
#                 "access": str(refresh.access_token),
#                     }
#         return Response(res, status=status.HTTP_201_CREATED)
    
class ApiOrder(generics.ListAPIView):
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, ExpiringTokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = order.objects.all()
        email = self.kwargs['email']
        token = self.request.META.get('HTTP_AUTHORIZATION')
        try:
            token = token.split(' ')
            token = token[1]
        except :
            token = None
            raise ValidationError(detail='Include Token')
        check = Token.objects.get(key=token)
        if check.user_id != email:
            raise ValidationError(detail='Email & Token not Match !')
        queryset = queryset.filter(user_id=email)
        return queryset
        
# return HttpResponseForbidden()      
class ApiLogout(APIView):
    authentication_classes = [SessionAuthentication, ExpiringTokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserSignoutSerializer(data = request.data)
        token_head = self.request.META.get('HTTP_AUTHORIZATION')
        try:
            token_head = token_head.split(' ')
            token_head = token_head[1]
        except :
            token_head = None
            raise ValidationError(detail='Include Token')
        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        token_client = request.data['token']
        try:
            check = Token.objects.get(key=token_client)
        except:
            check = None
            return Response({'Status':'Token not registered'}, status = status.HTTP_400_BAD_REQUEST)
        if check.key != token_head :
            return Response({'Status':'Head & Body not Match ! ?'}, status = status.HTTP_400_BAD_REQUEST)
        email = check.user_id
        print(email)
        check.delete()
        usr = user.objects.get(email=email)
        usr.is_login = False
        usr.save()
        return Response({'Status':'Sukses'}, status = status.HTTP_200_OK)
        
class ApiCheckOut(APIView):
    authentication_classes = [SessionAuthentication, ExpiringTokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_class = (FileUploadParser,)
    def post(self, request):
        serializer = CheckOutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ApiPay(APIView):
    authentication_classes = [SessionAuthentication, ExpiringTokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        payment = Payment({
                "intent": "sale",

                # Set payment method
                "payer": {
                    "payment_method": "paypal"
                },

                # Set redirect URLs
                "redirect_urls": {
                    "return_url": "http://creativectors.com",
                    "cancel_url": "http://creativectors.com"
                },

                # Set transaction object
                "transactions": [{
                    "amount": {
                    "total": request.data['total'],
                    "currency": "USD"
                    },
                    "description": request.data['total']
                }]
                })
        if payment.create():
                # Extract redirect url
            print(payment)
            for link in payment.links:
                print(link)
                if link.method == "REDIRECT":
                # Capture redirect url
                    redirect_url = (link.href)
                    print('-------------------------------')
                    print(redirect_url)
                # Redirect the customer to redirect_url
                else:
                    print("Error while creating payment:")
                    print(payment.error)
        return Response({"url":redirect_url}, status=status.HTTP_200_OK)
    
class ApiCarousel(generics.ListAPIView):
    serializer_class = CarouselSerializer
    def get_queryset(self):
        queryset= carousel.objects.all().order_by('-carousel_position')
        return queryset

class ApiGallery(generics.ListAPIView):
    serializer_class = GallerySerializer
    def get_queryset(self):
        queryset = gallery.objects.all()
        types = self.request.query_params.get('type', None)
        if types is not None:
            queryset.filter(type_gallery=types)
        return queryset