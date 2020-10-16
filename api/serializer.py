from rest_framework import serializers
from api.models import category, order, style, types, user

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = types
        fields = ('id','style_id','type_name','type_icon')

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = style
        fields = ('id','category_id','style_name','style_price','style_icon')

class CategorySerializer(serializers.ModelSerializer):
    styles = StyleSerializer(many=True)
    class Meta:
        model = category
        fields = ('id','category_name','category_icon','styles')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('email','full_name','date_join')

class OrderSeriliazer(serializers.ModelSerializer):
    key_user = serializers.CharField(source='user.c_user')
    class Meta:
        model = order
        fields = ('order_id','user_id','key_user','date_request','style_id','order_image','order_result','is_remove_acc','is_include_file','is_fast','is_payed','is_finish')
    