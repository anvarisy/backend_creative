from rest_framework import serializers
from api.models import carousel, category, gallery, order, style, types, user
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

# from rest_framework.authtoken.models import Token
UserModel = get_user_model()
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = types
        fields = ('id','style_id','type_name','type_icon','type_extra')

class StyleSerializer(serializers.ModelSerializer):
    styles = TypeSerializer(many=True)
    class Meta:
        model = style
        fields = ('id','category_id','style_name','style_price','style_icon','styles')

class CategorySerializer(serializers.ModelSerializer):
    categories = StyleSerializer(many=True)
    class Meta:
        model = category
        fields = ('id','category_name','category_icon','categories')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        # Atribut yang akan  diinput atau direturn sebagai data  saat post
        fields = ('email','full_name','date_joined','password')

    def create(self, validated_data):
        client = UserModel.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
        )
        client.set_password(validated_data['password'])
        client.save()
        print(client)
        return client


class OrderSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category_name')
    style_name = serializers.CharField(source='style.style_name')
    type_name = serializers.CharField(source='types.type_name')
    class Meta:
        model = order
        fields = ('order_id','user_id',
                  'category_id','category_name',
                  'style_id','style_name',
                  'types_id','type_name',
                  'date_request','order_image',
                  'num_character','note',
                  'is_remove_acc','is_include_file','is_fast','is_payed','is_finish','order_result','total')
        
class UserSigninSerializer(serializers.Serializer):
    email = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

class UserSignoutSerializer(serializers.Serializer):
    token = serializers.CharField(required = True)
    
class CheckOutSerializer(serializers.Serializer):
    order_id = serializers.CharField(default=get_random_string(10))
    user_id = serializers.CharField()
    category_id = serializers.IntegerField()
    style_id = serializers.IntegerField()
    types_id = serializers.IntegerField()
    order_image = serializers.ImageField()
    is_remove_acc = serializers.BooleanField()
    is_include_file = serializers.BooleanField(default=False)
    is_fast = serializers.BooleanField(default=False)
    total = serializers.IntegerField(default=0)
    num_character = serializers.IntegerField(default=1)
    note = serializers.CharField()
    def create(self, validated_data):
        o = order.objects.create(**validated_data)
        o.save()
        return o

class PaymentSerilizer(serializers.Serializer):
    order_id = serializers.CharField(required = True)
    total = serializers.IntegerField()

class CarouselSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = carousel
        fields = ('carousel_image','carousel_text','carousel_link','carousel_position')

class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = gallery
        fields = ('id', 'image_gallery','type_gallery')